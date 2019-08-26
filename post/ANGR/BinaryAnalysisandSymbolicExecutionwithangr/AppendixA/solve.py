# reference : https://web.wpi.edu/Pubs/E-project/Available/E-project-101816-114710/unrestricted/echeng_mqp_angr.pdf
# problem   : Appendix A
# solution  : Got target address from GDB tool. and angr script. modified original script because of some angr error.
import angr

proj = angr.Project('x86dym')
state = proj.factory.entry_state()
sm = proj.factory.simulation_manager(state)
pathgroup = sm.explore(find=0x004006ed, avoid=0x004006fc)
# I've got target address in GDB tool.
# 0x004006ed : address for "printf("Access granted!\n"); return 1;"
# 0x004006fc : address for "printf("Access denied.\n"); return 0;"
print(pathgroup)
print(pathgroup.found[0].posix.dumps(0).split(b'\x00')[0])

