import OlivOS
import OlivOSPluginTemplate

class Event(object):
    def init(self, Proc):
        pass

    def private_message(self, Proc):
        unity_reply(self, Proc)

    def group_message(self, Proc):
        unity_reply(self, Proc)

    def poke(self, Proc):
        poke_reply(self, Proc)

    def save(self, Proc):
        pass

    def menu(self, Proc):
        pass

def unity_reply(plugin_event, Proc):
    if plugin_event.data.message in [
        '/bot',
        '.bot',
        '[CQ:at,qq=' + str(plugin_event.base_info['self_id']) + '] .bot',
    ]:
        plugin_event.reply('OlivOSPluginTemplate')

def poke_reply(plugin_event, Proc):
    if plugin_event.data.target_id == plugin_event.base_info['self_id']:
        plugin_event.reply('OlivOSPluginTemplate')
    elif plugin_event.data.target_id == plugin_event.data.user_id:
        plugin_event.reply('OlivOSPluginTemplate')
    elif plugin_event.data.group_id == -1:
        plugin_event.reply('OlivOSPluginTemplate')

