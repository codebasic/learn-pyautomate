import zipfile
import sys, platform, os

class wZipFile(zipfile.ZipFile):
    def __init__(self, file, mode='r', compression=zipfile.ZIP_DEFLATED,
                 allowZip64=True):
        super().__init__(file, mode, compression, allowZip64)
        self._update_filenames()

    def _update_filenames(self):
        for info in super().infolist():
            info.filename = self._filename_from_bytes(info.filename)

    def _encode_decode_dance(self, text, enc, dec):
        return text.encode(enc).decode(dec)

    def _filename_from_bytes(self, filename):
        try:
            filename = filename.encode('utf-8').decode(sys.stdout.encoding)
            return filename
        except UnicodeDecodeError:
            try:
                filename = filename.encode('cp437').decode(sys.stdout.encoding)
                return filename
            except UnicodeEncodeError:
                return filename
            except:
                raise

    def _filename_to_bytes(self, filename):
        if platform.system() == 'Windows':
            filename = filename.encode(sys.stdout.encoding).decode('cp437')
        return filename

    def getinfo(self, name):
        try:
            info = super().getinfo(name)
        except KeyError:
            try:
                name = self._filename_to_bytes(name)
                info = super().getinfo(name)
            except:
                raise

        return info
