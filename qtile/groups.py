from libqtile.config import Group, Match
from icons import group_icons

class CreateGroups:
    group_names = group_icons 

    def init_groups(self):
        """
        Return the groups of Qtile
        """
        #### First and last
        groups = [
            Group(
                self.group_names[0],
                layout="max",
                matches=[Match(wm_class="brave-browser")]
            ),
            Group(
                self.group_names[1],
                layout="monadtall",
                matches=[Match(wm_class="Gnome-terminal")]
            ),
            Group(
                self.group_names[2],
                layout="monadtall",
                matches=[Match(wm_class="code")]
            ),
            Group(
                self.group_names[3],
                layout="monadtall",
            ),
            Group(
                self.group_names[4],
                layout="max",
                matches=[Match(wm_class="discord")]
            ),
            Group(
                self.group_names[5],
                layout="max",
                matches=[Match(wm_class="spotify")]
            )
        ]
        return groups

