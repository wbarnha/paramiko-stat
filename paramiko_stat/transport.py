# Copyright (C) 2003-2007  Robey Pointer <robeypointer@gmail.com>
#
# This file is part of Paramiko.
#
# Paramiko is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Paramiko is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Paramiko; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA.


from paramiko.transport import Transport as _Transport

from .sftp_client import SFTPClient


class Transport(_Transport):
    def open_sftp_client(self):
        """
        Create an SFTP client channel from an open transport.  On success, an
        SFTP session will be opened with the remote host, and a new
        `.SFTPClient` object will be returned.

        :return:
            a new `.SFTPClient` referring to an sftp session (channel) across
            this transport
        """
        return SFTPClient.from_transport(self)
