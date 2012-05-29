import Framework

class Hook( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.hook = self.g.get_user().get_repo( "PyGithub" ).get_hook( 257993 )

    def testAttributes( self ):
        self.assertEqual( self.hook.active, True ) # WTF
        self.assertEqual( self.hook.config, { "url": "http://foobar.com" } )
        self.assertEqual( self.hook.created_at, "2012-05-19T06:01:45Z" )
        self.assertEqual( self.hook.events, [ "push" ] )
        self.assertEqual( self.hook.id, 257993 )
        self.assertEqual( self.hook.last_response.status, "ok" )
        self.assertEqual( self.hook.last_response.message, "OK" )
        self.assertEqual( self.hook.last_response.code, 200 )
        self.assertEqual( self.hook.name, "web" )
        self.assertEqual( self.hook.updated_at, "2012-05-29T18:49:47Z" )
        self.assertEqual( self.hook.url, "https://api.github.com/repos/jacquev6/PyGithub/hooks/257993" )

    def testEditWithMinimalParameters( self ):
        self.hook.edit( "web", { "url": "http://foobar.com/hook" } )
        self.assertEqual( self.hook.config, { "url": "http://foobar.com/hook" } )
        self.assertEqual( self.hook.updated_at, "2012-05-19T05:08:16Z" )

    def testDelete( self ):
        self.hook.delete()

    def testTest( self ):
        self.hook.test() # This does not update attributes of hook

    def testEditWithAllParameters( self ):
        self.hook.edit( "web", { "url": "http://foobar.com" }, events = [ "fork", "push" ] )
        self.assertEqual( self.hook.events, [ "fork", "push" ] )
        self.hook.edit( "web", { "url": "http://foobar.com" }, add_events = [ "push" ] )
        self.assertEqual( self.hook.events, [ "fork", "push" ] )
        self.hook.edit( "web", { "url": "http://foobar.com" }, remove_events = [ "fork" ] )
        self.assertEqual( self.hook.events, [ "push" ] )
        self.hook.edit( "web", { "url": "http://foobar.com" }, active = True )
        self.assertEqual( self.hook.active, True )
