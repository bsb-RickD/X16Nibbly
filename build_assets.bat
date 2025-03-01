@echo off

echo ============= intro assets ====================

copy /b ..\intro_screen.bin+..\intro_tiles.bin+..\intro_sprites_base.bin assets\intro_data.raw
lzsa -v -r -f2 assets\intro_data.raw assets\intro_data.bin
del assets\intro_data.raw
lzsa -v -r -f2 ..\intro_sprites.bin assets\intro_sprites.bin
copy ..\intro_sprites_base.inc intro\intro_sprites_base.inc
copy ..\intro_sprites.inc intro\intro_sprites.inc
copy ..\intro_palette.bin assets
copy ..\intro_palette_mapping.bin assets
echo.

echo ============= travel assets ====================

copy /b ..\travel_screen.bin+..\travel_tiles.bin+..\travel_common_sprites.bin assets\travel_data.raw
lzsa -v -r -f2 assets\travel_data.raw assets\travel_data.bin
del assets\travel_data.raw

lzsa -v -r -f2 ..\travel_desert_sprites.bin assets\travel_desert_sprites.bin
lzsa -v -r -f2 ..\travel_green_sprites.bin assets\travel_green_sprites.bin
lzsa -v -r -f2 ..\travel_ice_sprites.bin assets\travel_ice_sprites.bin
lzsa -v -r -f2 ..\travel_volcano_sprites.bin assets\travel_volcano_sprites.bin

copy ..\travel_palette.bin assets
copy ..\travel_green_sprites.inc travel\travel_landscape_sprites.inc
copy ..\travel_*_pal_indexes.inc travel
copy ..\travel_common_sprites.inc travel\travel_common_sprites.inc
echo.


echo ============= playfield assets ====================

lzsa -v -r -f2 ..\wall_gfx_set_1.bin assets\wall_gfx_set_1.bin
lzsa -v -r -f2 ..\wall_gfx_set_2.bin assets\wall_gfx_set_2.bin
lzsa -v -r -f2 ..\wall_gfx_set_3.bin assets\wall_gfx_set_3.bin
lzsa -v -r -f2 ..\wall_gfx_set_4.bin assets\wall_gfx_set_4.bin
lzsa -v -r -f2 ..\wall_gfx_set_5.bin assets\wall_gfx_set_5.bin
lzsa -v -r -f2 ..\wall_gfx_set_6.bin assets\wall_gfx_set_6.bin
lzsa -v -r -f2 ..\wall_gfx_set_7.bin assets\wall_gfx_set_7.bin
copy ..\palette_gfx*.bin assets
echo.

