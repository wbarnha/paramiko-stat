from paramiko.client import SSHClient as _SSHClient


class SSHClient(_SSHClient):
    
    def open_sftp(self):
        """
        Open an SFTP session on the SSH server.

        :return: a new `.SFTPClient` session object
        """
        return self._transport.open_sftp_client()
