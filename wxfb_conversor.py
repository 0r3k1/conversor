# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Conversor
###########################################################################

class Conversor ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Conversor", pos = wx.DefaultPosition, size = wx.Size( 344,129 ), style = wx.DEFAULT_FRAME_STYLE|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 344,129 ), wx.Size( 344,129 ) )
		self.SetBackgroundColour( wx.Colour( 179, 217, 255 ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		tipoChoices = []
		self.tipo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, tipoChoices, 0 )
		self.tipo.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer3.Add( self.tipo, 1, wx.ALL, 5 )


		bSizer2.Add( bSizer3, 0, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.entrada = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.entrada, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		unidad1Choices = []
		self.unidad1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, unidad1Choices, 0 )
		bSizer4.Add( self.unidad1, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )


		bSizer9.Add( bSizer4, 1, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer9.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		self.salida = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.salida.Enable( False )

		bSizer41.Add( self.salida, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		unidad2Choices = []
		self.unidad2 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, unidad2Choices, 0 )
		bSizer41.Add( self.unidad2, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )


		bSizer9.Add( bSizer41, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer9, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tipo.Bind( wx.EVT_COMBOBOX, self.tipoUpdate )
		self.entrada.Bind( wx.EVT_TEXT, self.entradaUpdate )
		self.unidad1.Bind( wx.EVT_TEXT, self.unidad1Update )
		self.unidad2.Bind( wx.EVT_TEXT, self.unidad2Update )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tipoUpdate( self, event ):
		event.Skip()

	def entradaUpdate( self, event ):
		event.Skip()

	def unidad1Update( self, event ):
		event.Skip()

	def unidad2Update( self, event ):
		event.Skip()
