# Copyright 2014 ONOP psvm@onop.org
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Psvm interface."""

from novaclient import base


class Psvm(base.Resource):
    """PSVM is a Physical Switch Vlan Manager."""

    def __repr__(self):
        "Psvm/__repr__()\n"
        return "<Psvm: %s>" % self.id

    def update(self, values):
        """Update the name and/or availability zone."""
        return self.manager.update(self, values)

    def delete(self):
        """Deletes the given psvm."""
        self.manager.delete(self)


class PsvmManager(base.ManagerWithFind):
    """PSVM is a Physical Switch Vlan Manager."""
    resource_class = Psvm

    def list(self):
        """Get a list of psvm."""
        return self._list('/os-psvm', 'psvms')

    def create(self, ip_addr, switch_cred_id):
        """Create a new psvm."""
        body = {'psvm': {'ip': ip_addr,
                         'switch_cred_id': switch_cred_id}}
        return self._create('/os-psvm', body, 'psvm')

    def get(self, psvm):
        """Get details of the specified psvm."""
        return self._get('/os-psvm/%s' % (base.getid(psvm)), "psvm")

    def get_details(self, psvm):
        """Get details of the specified psvm."""
        return self.get(psvm)

    def update(self, psvm, values):
        """Update the details of a psvm."""
        body = {'psvm': values}
        return self._update("/os-psvm/%s" % base.getid(psvm),
                            body,
                            "psvm")

    def delete(self, psvm):
        """Delete the specified psvm."""
        self._delete('/os-psvm/%s' % (base.getid(psvm)))
