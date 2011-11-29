#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import urllib
import base64
from xml.dom import minidom

class MainHandler(webapp.RequestHandler):
    def get(self):
		#SET: campfire API key
		apikey = "" 
		
		#SET: campfire subdomain. If your domain is example.campfirenow, set to example
		subdomain = "" 
		
		#SET: campfire room id
		room_id = "" 
		
		response = urllib.urlopen("http://hourlypuppy.com/feed")
		
		#Extract the image URL from the RSS feed.
		pupdom = minidom.parseString( response.read().replace("&lt;","<").replace("&gt;",">") )
		pup = pupdom.getElementsByTagName("img")[0].getAttribute("src")
		
		#Prepare the puppy payload
		form_fields = '{"message":{"type":"TextMessage", "body":"' + pup +'"}}'
		
		#Post image to campfire room
		urlfetch.fetch( url="https://"+ subdomain +".campfirenow.com/room/"+ room_id +"/speak.json", payload=form_fields,  method=urlfetch.POST, headers={'Content-Type': 'application/json', "Authorization": "Basic "+base64.b64encode(apikey + ':x') })


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=False)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
