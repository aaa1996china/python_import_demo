import sys
pre_game_modules = set(sys.modules.keys())
def show_add_modules(step):
    res=[]
    for mname in list(sys.modules.keys()):
        if mname not in pre_game_modules:
            res.append(mname)
    print(step,res)