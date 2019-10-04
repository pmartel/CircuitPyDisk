#import the file you would like to have running
# this lets you modify the file without recopying it
#progStr = "scope_xy_adafruitlogo"
#progStr = "Lissajous1a"
#progStr = "LissajousRT"
progStr = "test"

print( "Running "+ progStr)
exec("import "+ progStr)