from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class ConfigurationValues(RelationBase):
    scope = scopes.GLOBAL

    auto_accessors = ['extra_db_config', 'auth_user', 'auth_query']

    @hook('{requires:pgbouncer-extra-config}-relation-joined')
    def joined(self):
        self.remove_state('{relation_name}.departed')
        self.set_state('{relation_name}.connected')

    @hook('{requires:pgbouncer-extra-config}-relation-changed')
    def changed(self):
        self.set_state('{relation_name}.available')

    @hook('{requires:pgbouncer-extra-config}-relation-departed')
    def departed(self):
        self.remove_state('{relation_name}.connected')
        self.remove_state('{relation_name}.available')
        self.set_state('{relation_name}.departed')

    def get_extra_db_config(self):
        return self.get_remote('extra_db_config')

    def get_auth_user(self):
        return self.get_remote('auth_user')

    def get_auth_query(self):
        return self.get_remote('auth_query')
