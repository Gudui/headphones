#  This file is part of Headphones.
#
#  Headphones is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Headphones is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Headphones.  If not, see <http://www.gnu.org/licenses/>.

# Parts of this file are a part of SickRage.
# Author: Mr_Orange <mr_orange@hotmail.it>
# URL: http://code.google.com/p/sickbeard/
# Adapted for Headphones by <noamgit@gmail.com>
# URL: https://github.com/noam09
#
# SickRage is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SickRage is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SickRage. If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from headphones import logger

import time
import re
import os
import json
import headphones
import requests
from base64 import b64encode
import traceback

delugeweb_auth = {}
delugeweb_url = ''
deluge_verify_cert = False
scrub_logs = True


def _scrubber(text):
    if scrub_logs:
        try:
            # URL parameter values
            text = re.sub('=[0-9a-zA-Z]*', '=REMOVED', text)
            # Local host with port
            # text = re.sub('\:\/\/.*\:', '://REMOVED:', text) # just host
            text = re.sub('\:\/\/.*\:[0-9]*', '://REMOVED:', text)
            # Session cookie
            text = re.sub("_session_id'\: '.*'", "_session_id': 'REMOVED'", text)
            # Local Windows user path
            if text.lower().startswith('c:\\users\\'):
                k = text.split('\\')
                text = '\\'.join([k[0], k[1], '.....', k[-1]])
            # partial_link = re.sub('(auth.*?)=.*&','\g<1>=SECRETZ&', link)
            # partial_link = re.sub('(\w)=[0-9a-zA-Z]*&*','\g<1>=REMOVED&', link)
        except Exception as e:
            logger.debug('Deluge: Scrubber failed: %s' % str(e))
    return text


def addTorrent(link, data=None, name=None):

def getTorrentFolder(result):
 


def removeTorrent(torrentid, remove_data=False):



def _get_auth():
 

def _add_torrent_magnet(result):



def _add_torrent_url(result):


def _add_torrent_file(result):


def setTorrentLabel(result):


def setSeedRatio(result):



def setTorrentPath(result):



def setTorrentPause(result):

