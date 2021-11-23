import json
from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class ConfigurationValues(RelationBase):
    scope = scopes.GLOBAL

    auto_accessors = ['section_extra_parameters']

    @hook('{requires:pgbouncer-extra-config}-relation-joined')
    def joined(self):
        self.remove_state('{relation_name}.departed')
        self.set_state('{relation_name}.connected')

    @hook('{requires:pgbouncer-extra-config}-relation-changed')
    def changed(self):
        if self.get_remote('section_extra_parameters'):
            self.set_state('{relation_name}.available')

    @hook('{requires:pgbouncer-extra-config}-relation-departed')
    def departed(self):
        self.remove_state('{relation_name}.connected')
        self.remove_state('{relation_name}.available')
        self.set_state('{relation_name}.departed')

    def section_extra_parameters(self):
        return json.loads(self.get_remote('section_extra_parameters'))
