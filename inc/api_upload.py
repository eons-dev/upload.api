import os
import logging
import apie

class upload(external):
    def __init__(this, name="upload"):
        super().__init__(name)

        this.supportedMethods = ['POST', 'PUT', 'PATCH']

        #this.allowedNext = ['help'] only

        this.helpText = '''\
Upload any file by offloading the actual work to another API.
This does not (currently) have access to the local filesystem.

Per the parent 'external':
'''
        this.helpText += super().helpText



    def Call(this):
        # This is a very simple wrapper at the moment.
        pass