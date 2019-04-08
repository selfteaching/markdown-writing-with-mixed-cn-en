#!/usr/bin/env python
import os
import re
import yaml
import click

# creating linted directory
linted_path = os.path.join(os.getcwd(), 'linted')

this_dir, this_filename = os.path.split(__file__)

try:
    os.mkdir(linted_path)
except FileExistsError:
    pass 
except OSError:
    print(f"Creation of linted directory {linted_path} failed.")

re_dict = {
    'a': 're.A',
    'i': 're.I',
    'l': 're.L'
}

@click.command()
@click.option(
    '-c',
    '--config-path',
    'config_path',
    default=this_dir,
    type=click.Path(),
    help='Specify directory that contains rules file.'
    )    
@click.option(
    '-l',
    '--log-file',
    'log_file',
    default=os.path.join(os.getcwd(), 'log.txt'),
    help='Specify file name for log, default: "log.txt".'
    )    
@click.option(
    '-f',
    '--fix-directly',
    'fix_directly',
    default=True,
    type=click.BOOL,
    help='Fix file(s) directly, rather than save to "/linted" directory. Default: True.'
    )
@click.option(
    '-r',
    '--rules-file-name',
    'rules_file_name',
    default='rules.yml',
    help='Specify rules file name. Default: rules.yml'
    )       
@click.option(
    '-v',
    '--verbose',
    'verbose',
    default=True,
    type=click.BOOL,
    help='Ask permission before fix. Default: True.'
    )        
@click.argument(
    'files',
    nargs=-1,
    type=click.Path()
    )

def cnenlinter(config_path, log_file, fix_directly, rules_file_name, verbose, files):

    rules_file = os.path.join(config_path, rules_file_name)

    with open(os.path.join(config_path, rules_file), 'r') as rf:
        rules = list(yaml.safe_load_all(rf.read()))

    log = ''
    logfile = open(log_file, 'w')

    for filename in files:

        with open(filename, 'r') as f:
            text = f.read()
            # replace concessive blank lines to single one
            pattern = re.compile(r"(\s*\n){3,}")
            text = pattern.sub('\n\n', text)
            lines = text.splitlines()
        f.close

        lines_linted = []

        for line in lines:

            linted = line.rstrip()
            temp = linted

            # ignore lines only consisting of asscii chars
            if not linted.isascii() or linted.startswith('#'):

                for rule in rules:
                    # accepted flag: a, i, l
                    expected_text = rule['expected'].split('/')
                    pattern_text = rule['pattern'].split('/')
                    if pattern_text[2] in ['a', 'i', 'l']:
                        flag = re_dict[pattern_text[2]]
                        pattern = re.compile(pattern_text[1], flag)
                    else: 
                        pattern = re.compile(pattern_text[1])

                    if pattern.findall(linted):
                        linted = pattern.sub(rule['expected'].strip('/'), linted)

                if temp != linted.rstrip(): 
                    log = f'\n\n{filename} (line {lines.index(line) + 1}):\n{line}\n=>\n{linted}'
                    print(log)

                    if verbose:
                        valid_permission = True
                        while valid_permission:
                            permission = input('fix this one? "y" or "n"? ')
                            if permission == 'y' or permission == 'n':
                                if permission == 'y':
                                    logfile.writelines(log + '\n**ACCEPTED!**\n')
                                elif permission == 'n':
                                    linted = temp
                                    logfile.writelines(log + '\n**REJECTED!**\n')
                                valid_permission = False
                            else:
                                valid_permission = True
                    else:
                        logfile.writelines(log + '\n**ACCEPTED!**\n')
            
            lines_linted.append(linted.rstrip())

        if fix_directly:
            file_to_save = filename
        else:
            file_to_save = os.path.join(linted_path, filename)

        with open(file_to_save, 'w') as r:
            for line_linted in lines_linted:
                r.writelines(line_linted + '\n')
        r.close

        logfile.close

if __name__ == '__main__':
    cnenlinter()