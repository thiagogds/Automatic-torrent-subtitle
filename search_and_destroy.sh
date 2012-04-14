curl -b $HOME/Development/Autosubs/cookies.txt --data "txtLegenda=$1&selTipo=1&int_idioma=1&btn_buscar.x=24&btn_buscar.y=7" http://legendas.tv/index.php?opcao=buscarlegenda > $HOME/Development/Autosubs/html

/usr/bin/python  $HOME/Development/Autosubs/parse_html.py

sleep 1

rm -rf /tmp/legendas/legendas.tv
/usr/local/bin/wget --mirror --load-cookies $HOME/Development/Autosubs/cookies.txt -P /tmp/legendas/ http://legendas.tv/info.php?d=`cat $HOME/Development/Autosubs/legenda_id.txt`&c=1

sleep 20

cd /tmp/legendas/legendas.tv
mv info\.php\?d\=`cat $HOME/Development/Autosubs/legenda_id.txt`\&c\=1 legenda.rar

/usr/local/Cellar/unrar/4.0.7/bin/unrar x legenda.rar $2
