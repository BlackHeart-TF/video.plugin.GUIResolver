import urlparse,sys
import urlresolver
import xbmcaddon,xbmcgui
params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

def search():
	t = xbmcaddon.Addon().getLocalizedString(32010).encode('utf-8')
	k = xbmc.Keyboard('', t) ; k.doModal()
	q = k.getText() if k.isConfirmed() else None
	if (q == None or q == ''): return
	media_url = urlresolver.resolve(q)
	if media_url == False: return
	listitem =xbmcgui.ListItem ('Link')
	listitem.setInfo('video', {'Title': media_url, 'Genre': 'internet'})
	xbmc.Player().play(media_url, listitem)

if action == None:
	search()
