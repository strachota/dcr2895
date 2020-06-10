###############################################################################
# FILE
#   default.cshrc
#
# DESCRIPTION
#   This is the .cshrc for CTBT Monitoring System (CMS) users.
#   It is specialised by mkCMSuser for one the following values
#   of CMS_MODE:    process   - pure process mode
#           analysis  - pure analysis mode
#           dual      - analysis mode for system managers
#           public    - analysis mode for the unprivileged
#
###############################################################################

########################################
##        System Specifics            ##
########################################

## CTBT Monitoring System
    setenv CMS_CONFIG           `pwd`

if ( ! $?CMS_MODE ) \
    setenv CMS_MODE     process # CMS user mode

## CTBT Monitoring System, SHI
setenv CMS_HOME     ${CMS_CONFIG}/../rel
setenv SHARED_HOME  ${CMS_CONFIG}/../shared
setenv CMS_SCRIPTS  ${CMS_CONFIG}/../scripts
setenv SHI_AUX      ${CMS_CONFIG}/../aux

## The Global Environment
source ${CMS_CONFIG}/system_specs/env/global.env
setenv PATH ${PATH}:.:${HOME}/bin

## Get the editor, printer, terminfo for the alternate screen buffer
setenv TERMINFO		${CMS_CONFIG}/system_specs/env/terminfo
setenv EDITOR		vi


########################################
##         User Specifics             ##
########################################
set history=100
limit core 10240 

#2016-06-16: set umask so that new files can only be written by auto (needed due to problems in Git)
umask 022



###########################################
## EXIT if not running interactively
###########################################
if( ! $?prompt ) exit 0

## Set the prompt
set prompt="`uname -n`-\!%"" "

## Set terminal options
set filec
stty erase  werase  kill  intr 

## Convenience aliases
alias   h       'history'
alias   lo      'logout'
alias   lsl     'ls -lF'
alias   lsa     'ls -aF'
alias   ls      'ls -F'

## ClearCase specific additions, particularly for processing engineers
## and automated system users, not for analysts
##
if ( $CMS_MODE != "analysis" ) then
    if( $?prompt ) then
        if( $?CLEARCASE_ROOT ) then
            set prompt = "[`basename $CLEARCASE_ROOT`] $prompt"
        endif
    endif
endif

## Set user aliases
if (-e ~/.alias) source ~/.alias

## Set user cshrc
if (-e ~/.cshrc.user) source ~/.cshrc.user

unset autologout
## Please do not remove -- GIT specifics ## Shaban
if ( $?GIT_USER ) then
        setenv GIT_AUTHOR_NAME "$GIT_USER"
        setenv GIT_AUTHOR_EMAIL `echo $GIT_USER | tr ' ' '.'`"@ctbto.org"
        setenv GIT_COMMITTER_NAME "$GIT_USER"
        setenv GIT_COMMITTER_EMAIL `echo $GIT_USER | tr ' ' '.'`"@ctbto.org"
	
	if (-e /usr/bin/git ) then 
		git config --global push.default current
	endif 
endif
umask 022
