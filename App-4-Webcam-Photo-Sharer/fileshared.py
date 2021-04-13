class Fileshared:
    """
    This class is to generated link and return link of share.
    """

    def __init__(
        self, filepath, api_key="AhPPmwO5RNCs73ebiq7zKz"):
        """
        Parameter filename need to provided which file want to share
        Parameter api_key as default provided. To generate api_key is need user
        to signup from www.filestack.com
        """
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        """
        Return generate link file
        """
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
