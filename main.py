import subprocess
import constants
import argparse

parser = argparse.ArgumentParser(description="Note: possible pairs are <LocalPath> <S3Uri> or <S3Uri> <LocalPath> or <S3Uri> <S3Uri>")

parser.add_argument('source_directory', help = 'Path you want to sync from.', type=str)
parser.add_argument('destination_directory', help = 'Path you want to sync to.', type=str)

def do_sync():
    """ sync s3 bucket """
    try:
        # parsing args
        args = parser.parse_args()
        SOURCE_DIR = args.source_directory
        DESTINATION_DIR = args.destination_directory

        print('Syncing from S3 [{}] to Local [{}]'.format(SOURCE_DIR, DESTINATION_DIR))
        command = ('aws', 's3', 'sync', SOURCE_DIR, DESTINATION_DIR)
        subprocess.check_output(command, )
    except subprocess.CalledProcessError as e:
        print(e.output)


if __name__ == "__main__":
    do_sync()