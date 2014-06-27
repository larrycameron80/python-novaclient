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

"""Psvmcred interface."""

from novaclient import base


class Psvmcred(base.Resource):
    """PSVM is a Physical Switch Vlan Manager."""

    def __repr__(self):
        "Psvmcred/__repr__()\n"
        return "<Psvmcred: %s>" % self.id

    def update(self, values):
        """Modify a psvm credential."""
        return self.manager.update(self, values)

    def delete(self):
        """Delete a psvm credential."""
        self.manager.delete(self)


class PsvmcredManager(base.ManagerWithFind):
    """Credentials for the Physical Switch Vlan Manager (PSVM)."""
    resource_class = Psvmcred

    def list(self):
        """Get a list of psvmcred."""
        return self._list('/os-psvmcred', 'psvmcreds')

    def create(self, user_name, password):
        """Create a new psvmcred."""
        body = {'psvmcred': {'user_name': user_name,
                             'password': password}}
        return self._create('/os-psvmcred', body, 'psvmcred')

    def get(self, psvmcred):
        """Get details of the specified psvmcred."""
        return self._get('/os-psvmcred/%s' % (base.getid(psvmcred)),
                         "psvmcred")

    def get_details(self, psvmcred):
        """Get details of the specified psvmcred."""
        return self.get(psvmcred)

    def update(self, psvmcred, values):
        """Update the details of a psvmcred."""
        return self._update("/os-psvmcred/%s" % base.getid(psvmcred),
                            {'psvmcred': values},
                            "psvmcred")

    def delete(self, psvmcred):
        """Delete the specified psvmcred."""
        self._delete('/os-psvmcred/%s' %
                     (base.getid(psvmcred)))
