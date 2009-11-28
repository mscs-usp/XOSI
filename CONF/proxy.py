import urllib2


password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
# créer un password manager

password_mgr.add_password(None,
    top_level_url, username, password)
# ajoute le username et password
# si on connaissait le domaine, on pourrait l'utiliser au lieu de ``None``

handler = urllib2.HTTPBasicAuthHandler(password_mgr)
# créer le handler

opener = urllib2.build_opener(handler)
# du handler vers  l'opener

opener.open(a_url)
# utilise l'opener pour ramener un URL

urllib2.install_opener(opener)
# installe l'opener
# maintenant tous les appels à urllib2.urlopen vont utiliser notre opener

proxy_support = urllib2.ProxyHandler({})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)





the_url = 'http://www.voidspace.org.uk'
req = urllib2.Request(the_url)
handle = urllib2.urlopen(req)
the_page = handle.read()

print the_page
