arg_1=`echo $1 | rev | cut -d . -f2- | rev | sed 's:/:.:g'`

REMOTE_DEBUG=1 python -m $arg_1 ${@:2}