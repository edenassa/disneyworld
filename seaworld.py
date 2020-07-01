sea_world_graph = {
    'Entrance & Exit': set(['Lost & Found','Bayside Stadium','Captain Petes Island Hot Dogs']),
    'Lost & Found': set(['Entrance & Exit','Bayside Stadium','Wild Arctic']),
    'Bayside Stadium': set(['Entrance & Exit','Lost & Found','Wild Arctic']),
    'Wild Arctic': set(['Lost & Found','Bayside Stadium','Shamu Stadium']),
    'Shamu Stadium':set(['Wild Arctic','Sea Garden',]),
    'Sea Garden':set(['Shamu Stadium','Nautilus Theater']),
    'Nautilus Theater':set(['Sea Garden','Sea Lion & Otter Theater']),
    'Sea Lion & Otter Theater':set(['Nautilus Theater','Antarctica','Sky Tower']),
    'Antarctica':set(['Sea Lion & Otter Theater','Journey To Atlantis','Kraken Roller Coaster']),
    'Kraken Roller Coaster':set(['Antarctica','Journey To Atlantis']),
    'Sky Tower':set(['Sea Lion & Otter Theater','Food court']),
    'Food court':set(['Sky Tower','Entrance & Exit']),
    'Journey To Atlantis':set(['Antarctica','Kraken Roller Coaster','Dolphin Theater']),
    'Dolphin Theater':set(['Journey To Atlantis','Captain Petes Island Hot Dogs',]),
    'Captain Petes Island Hot Dogs':set(['Entrance & Exit','Dolphin Theater'])








}