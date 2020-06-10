# @(#)idcdacs/dacsctrl.bashrc
###############################################################################
#
# Default IDC/SHI DACS configuration file for the dacsctrl utility.
#
###############################################################################

# Roles
#
# Constraint: Role names must be unique because they are used as keys
# in the associative arrays defined herein.

role_list="
db_rabbit
TI-detpro TI-late TI-dtkpmcc TI-dtkpmcc-late StaPro
DtkPmcc DtkPmcc-late
"

# Execution programs

program[db_rabbit]="db_rabbit"
program[TI-detpro]="tis_rabbit"
program[TI-dtkpmcc]="tis_rabbit"
program[TI-dtkpmcc-late]="tis_rabbit"
program[TI-late]="tis_rabbit"
program[DtkPmcc]="tortoise"
program[DtkPmcc-late]="tortoise"
program[StaPro]="tortoise"

# Command parameter files
#
# Constraint: The combination of program[role] and par[role] must be
# unique so that program instances can be identified from the output
# of 'ps'.

par[db_rabbit]="db_rabbit/db_rabbit.par"
par[TI-detpro]="tis_rabbit/tis.par"
par[TI-dtkpmcc]="tis_rabbit/tis-dtkpmcc.par"
par[TI-dtkpmcc-late]="tis_rabbit/tis-dtkpmcc-late.par"
par[TI-late]="tis_rabbit/tis-late.par"
par[DtkPmcc]="tortoise/detpro/tortoise-DtkPmcc.par"
par[DtkPmcc-late]="tortoise/detpro/tortoise-DtkPmcc-late.par"
par[StaPro]="tortoise/detpro/tortoise-StaPro.par"

# Command arguments

args[db_rabbit]="par=$configdir/${par[db_rabbit]}"
args[TI-detpro]="par=$configdir/${par[TI-detpro]}"
args[TI-dtkpmcc]="par=$configdir/${par[TI-dtkpmcc]}"
args[TI-dtkpmcc-late]="par=$configdir/${par[TI-dtkpmcc-late]}"
args[TI-late]="par=$configdir/${par[TI-late]}"
args[DtkPmcc]="par=$configdir/${par[DtkPmcc]}"
args[DtkPmcc-late]="par=$configdir/${par[DtkPmcc-late]}"
args[StaPro]="par=$configdir/${par[StaPro]}"

# Nominal number of processes

autostart[db_rabbit]=1    # must never be more than one!
autostart[TI-detpro]=1
autostart[TI-dtkpmcc]=1
autostart[TI-dtkpmcc-late]=1
autostart[TI-late]=1
autostart[DtkPmcc]=5
autostart[DtkPmcc-late]=2
autostart[StaPro]=10
