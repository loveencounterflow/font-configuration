


# FontConfig Font Configuration

The file `fonts.conf` should be saved as `~/.config/fontconfig/fonts.conf`. If you want to
keep both the file under version control *and* have live-reload on configuration change,
hardlink `~/.config/fontconfig/fonts.conf` to `fonts.conf`:

```bash
mkdir -p ~/.config/fontconfig
cd ~/.config/fontconfig
ln ~/path/to/font-configuration/fonts.conf
```

Live reload only gets a chance when you open the file in your editor as `~/.config/fontconfig/fonts.conf`;
changes to *same* underlying file system object using the other path will only be picked up when e.g.
closing the terminal emulator and re-opening it (at least that's what I got with terminator).

For the DTD see https://github.com/behdad/fontconfig/blob/master/fonts.dtd

...


```bash
➜  mojikura (master) locate greciliae
/usr/local/texlive/2016/texmf-dist/fonts/source/gregoriotex/greciliae-base.sfd
/usr/local/texlive/2016/texmf-dist/fonts/truetype/public/gregoriotex/greciliae-op.ttf
/usr/local/texlive/2016/texmf-dist/fonts/truetype/public/gregoriotex/greciliae.ttf
```

also see https://wiki.archlinux.org/index.php/Font_configuration/Examples

thx to https://wiki.archlinux.org/index.php/Font_configuration
for the rejectfont syntax

```xml
<rejectfont><glob>/usr/local/texlive/2016/texmf-dist/fonts/*</glob></rejectfont>
<rejectfont><pattern><patelt name="family"><string>gregorio</string></patelt></pattern></rejectfont>
```


