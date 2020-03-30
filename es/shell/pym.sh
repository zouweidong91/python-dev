arg_1=`echo $1 | rev | cut -d . -f2- | rev | sed 's:/:.:g'`

python -m $arg_1 ${@:2}