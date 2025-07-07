# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import logging

from awscli.customizations.s3.subcommands import NO_OVERWRITE
from awscli.customizations.s3.syncstrategy.base import BaseSync
from awscli.customizations.utils import uni_print

LOG = logging.getLogger(__name__)



class NoOverwriteSync(BaseSync):
    ARGUMENT=  NO_OVERWRITE

    def determine_should_sync(self, src_file, dest_file):

        if not dest_file:
            # If the file doesn't exist at the destination, sync it
            LOG.debug(
                "syncing: %s -> %s, file does not exist at destination",
                src_file.src,
                src_file.dest,
            )

            return True
        else:
            # If the file exists at both source and destination, don't sync it
            # and generate a warning message
            LOG.debug(
                "skipping: %s -> %s, file exists at destination",
                src_file.src,
                src_file.dest,
            )
            uni_print(
            f"warning: Skipping file {src_file.src} as it already exists on {src_file.dest}\n"
            )
            
            return False




