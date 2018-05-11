import sys
import click

@click.command()
@click.argument('file', type=click.File('rb'))
def dump_file(file):
    sys.stdout.write('"')
    for read_chunk in file.read(1024):
        outbuffer=bytes()
        for i in read_chunk:
            if i == '\n':
                outbuffer += '\\n'
            elif i == '"':
                outbuffer += '\\"'
            elif i == '\\':
                outbuffer += '\\\\'
            elif ord(i) < ord(' ') or ord(i) > ord('~'):
                outbuffer += '\\x%02x' % ord(i)
            else:
                outbuffer += i
        sys.stdout.write(outbuffer)
    sys.stdout.write('"\n')

if __name__ == '__main__':
    dump_file()
