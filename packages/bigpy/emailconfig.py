# Copyright 2016 Codebasic.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
     # http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import os
import configparser
import argparse
import subprocess

def get_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def update_config(config_filename, config, verbose=False):
    with open(config_filename, 'w') as cf:
        config.write(cf)
    if verbose:
        print('Config file {} updated.'.format(config_filename))

def get_access_token(config_file, section, refresh=False):
    if refresh:
        refresh_access_token(config_file, section)
    config = get_config(config_file)
    return config[section]['access_token']

def refresh_access_token(configpath, section):
    config = get_config(configpath)
    user = config[section]['user']
    client_id = config[section]['client_id']
    client_secret = config[section]['client_secret']
    refresh_token = config[section]['refresh_token']
    # gmail oauth2.py is written for python 2
    ps = subprocess.run([
        os.path.join(os.path.dirname(__file__), './gmail/oauth2.py'),
        '--user={}'.format(user),
        '--client_id={}'.format(client_id),
        '--client_secret={}'.format(client_secret),
        '--refresh_token={}'.format(refresh_token)],
        stdout=subprocess.PIPE)
    access_token = ps.stdout.decode('utf-8').split('\n')[0].split(':')[1]
    print('접근 토큰: {}'.format(access_token))

    # update config file
    config[section]['access_token'] = access_token
    update_config(configpath, config, verbose=True)

def main(argv, debug=False):
    parser = argparse.ArgumentParser(description='Gmail 접속 권한 설정')
    parser.add_argument('command', action='store',
        help='init|refresh|test')
    parser.add_argument('--configpath', action='store')
    args = parser.parse_args()

    if args.command == 'init':
        print('Gmail 접근 권한 요청 중 ...')
        return

    # refresh access token
    if args.command == 'refresh':
        if not args.configpath:
            print('설정 파일 경로 지정이 필요합니다.')
            sys.exit(1)
        configpath = os.path.abspath(args.configpath)
        refresh_access_token(configpath, 'GMAIL')

    # TODO: check if access_token valid

if __name__ == '__main__':
    main(sys.argv, True)
