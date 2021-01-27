# Copyright 2021 Patricio Cordero
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import os, sys, argparse

def parse_args():
    parser = argparse.ArgumentParser(description='MasterKey')

    parser.add_argument('action', type=str, help='Is the action to do. (default:get)', choices=['add', 'remove', 'get', 'genkey'], default='get')
    parser.add_argument('-l','--lock', type=str, help='Is the name or code of the lock to open')

    parser.set_defaults(action='get')

    return parser.parse_args()


def main():
    args = parse_args()
    from masterkey.masterkey import Masterkey
    obj = Masterkey()


    if args.action == 'get':
        obj.get(args.lock)
        pass
    if args.action == 'add':
        obj.add()
        pass
    if args.action == 'remove':
        obj.remove(args.lock)
        pass
    if args.action == 'genkey':
        obj.generatekey()
        pass
    pass

if(__name__) == '__main__':
    main()
