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

"""Psvmpbind interface."""

from novaclient import base


class Psvmpbind(base.Resource):
    """Physical Switch Vlan Manager Port Bind."""

    def __repr__(self):
        "Psvmpbind/__repr__()\n"
        return "<Psvmpbind: %s>" % self.id

    def update(self, values):
        """Update the details of a psvmbind."""
        return self.manager.update(self, values)

    def delete(self):
        """Delete a psvmbind."""
        self.manager.delete(self)


class PsvmpbindManager(base.ManagerWithFind):
    """Port Bind data for the Physical Switch Vlan Manager (PSVM)."""
    resource_class = Psvmpbind

    def list(self):
        """Get a list of psvmpbind."""
        return self._list('/os-psvmpbind', 'psvmpbinds')

    def create(self, switch_id, compute_node_id, switch_port):
        """Create a new psvmpbind."""
        body = {'psvmpbind':
                {'switch_id': switch_id,
                 'compute_node_id': compute_node_id,
                 'switch_port': switch_port}}
        return self._create('/os-psvmpbind', body, 'psvmpbind')

    def get(self, psvmpbind):
        """Get details of the specified psvmpbind."""
        return self._get('/os-psvmpbind/%s' % (base.getid(psvmpbind)),
                         "psvmpbind")

    def get_details(self, psvmpbind):
        """Get details of the specified psvmpbind."""
        return self.get(psvmpbind)

    def update(self, psvmpbind, values):
        """Update the details of a psvmpbind."""
        return self._update("/os-psvmpbind/%s" % base.getid(psvmpbind),
                            {'psvmpbind': values},
                            "psvmpbind")

    def delete(self, psvmpbind):
        """Delete the specified psvmpbind."""
        self._delete('/os-psvmpbind/%s' %
                     (base.getid(psvmpbind)))
