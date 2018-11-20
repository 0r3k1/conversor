#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Converosr

import wx
from wxfb_conversor import Conversor

unidades = ( "Longitud", "Masa", "Energia", "Tiempo")
unidadesL = ("Milimetro", "Centimetro", "pies", "Metro", "Yarda", "Pulagada")
unidadesM = ("Gramos", "Miligramos", "Libras", "Onzas", "Kilogramo")
unidadesE = ("Julio", "Kilojoule", "Gram Calorie", "Kilocaloria", "Vatio-Hora", "Kilovatio-Hora")
unidadesT = ("Segundo", "Minuto", "Nanosegundo", "Microsegundo", "Milisegundo", "Hora", "Dia", "Semana")

dic_unidades = {"Longitud": unidadesL, "Masa": unidadesM, "Energia": unidadesE, "Tiempo": unidadesT}

longitud = (1, 10, 304.8, 1000, 914.4, 25.4)
masa = (1, 0.001, 453.592, 28.3495, 1000)
energia = (1, 1000, 4.184, 4184, 3600, 3600000)
tiempo = (1, 60, 0.000000001, 0.000001, 0.001, 3600, 86400, 604800)

def regla_de_tres(a=1, b=1, c=1):
    return (a*b)/c

def is_number(s):
    try:
        int(s)
        float(s)
        return True
    except ValueError:
        return False

def toMilimetros(e, c):
    x = unidadesL.index(e)
    return regla_de_tres(a=c, b=longitud[x])

def milimetrosTo(s, c):
    x = unidadesL.index(s)
    return regla_de_tres(a=c, c=longitud[x])

def toMasa(e, c):
    x = unidadesM.index(e)
    return regla_de_tres(a=c, b=masa[x])

def masaTo(s, c):
    x = unidadesM.index(s)
    return regla_de_tres(a=c, c=masa[x])

def toEnergia(e, c):
    x = unidadesE.index(e)
    return regla_de_tres(a=c, b=energia[x])

def energiaTo(s, c):
    x = unidadesE.index(s)
    return regla_de_tres(a=c, c=energia[x])

def toTiempo(e, c):
    x = unidadesT.index(e)
    return regla_de_tres(a=c, b=tiempo[x])

def tiempoTo(s, c):
    x = unidadesT.index(s)
    return regla_de_tres(a=c, c=tiempo[x])


class win_conversor(Conversor):
    def __init__(self, parent):
        Conversor.__init__( self, parent)
        self.SetIcon(wx.Icon(wx.IconLocation("icon.ico")))
        self.entrada.SetValue("1")
        self.appen_tipo()
        self.appen_unidades(dic_unidades[unidades[0]])

    def appen_tipo(self):
        for i in unidades:
            self.tipo.Append(i)
        self.tipo.SetValue(self.tipo.GetString(0))

    def appen_unidades(self, lista):
        self.unidad1.Clear()
        self.unidad2.Clear()

        for i in lista:
            self.unidad1.Append(i)
            self.unidad2.Append(i)
        self.unidad1.SetValue(self.unidad1.GetString(0))
        self.unidad2.SetValue(self.unidad2.GetString(1))
        self.entrada.SetValue("1")

    def conversor(self):
        tipo = self.tipo.GetValue()

        c = int(self.entrada.GetValue())
        s = self.unidad2.GetValue()
        e = self.unidad1.GetValue()
        r = None

        if tipo == "Longitud":
            r = milimetrosTo(s, toMilimetros(e, c))
        if tipo == "Masa":
            r = masaTo(s, toMasa(e, c))
        if tipo == "Energia":
            r = energiaTo(s, toEnergia(e, c))
        if tipo == "Tiempo":
            r = tiempoTo(s, toTiempo(e, c))

        self.salida.SetValue("{0}".format(r))


    def tipoUpdate(self, event):
        self.appen_unidades(dic_unidades[unidades[self.tipo.GetSelection()]])
        event.Skip()

    def entradaUpdate(self, event):
        if not self.entrada.IsEmpty():
            e = self.entrada.GetValue()
            if is_number(e):
                self.conversor()
            else:
                e = e[:-1]
                self.entrada.SetValue(e)

    def unidad1Update(self, event):
        self.conversor()
        event.Skip()

    def unidad2Update( self, event ):
        self.conversor()
        event.Skip()
