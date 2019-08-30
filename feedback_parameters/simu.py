#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:39:16 2019

@author: ahoudevi
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""
parameters:
    g : gravity acceleration [m.s^-2]
    m : float mass [kg]
    a : float added mass [no dimension]
    r : float radius [m]
    L : float length [m]
    V : float volume [m^3] (optional)
    rho_w : water density [kg.m^3]
    omega :  current rotation rate [rad/s]
    lead : screw lead (i.e. displacement after one screw revolution) [m]
    r_piston : piston radius [m]
    u : piston flow [m^3.s^-1]
"""

def omega2dvdt(omega=12.4*2.*np.pi/360., lead=0.0175, r_piston=0.025):

    """
    Function computing the piston flow u
    
    parameters:
        omega: float [rad/s]
            current rotation rate, omega=dphi/dt
            for ENSTA float, omega_max = 124.*2.*np.pi/60.,
            omega_min = 12.4*2.*np.pi/60.
        lead: float [m]
            screw lead (i.e. displacement after one screw revolution)
            d = phi/2/pi x lead
        r_piston: float [m]
            piston radius
    """
    return omega*lead/2.*r_piston**2

g = 9.81 #m.^s-2
rho_w = 997 #kg.m^3

params = {'r': 0.06, 'L': 0.5, 'a': 1., 'omega' : 12.4*2.*np.pi/360., 'lead' : 0.0175, 'r_piston' : 0.025}
params['m'] = 1000. * np.pi * params['r'] ** 2 * params['L']
if 'V' not in params:
    params['V'] = np.pi*params['r']**2*params['L']
    
params['u'] = omega2dvdt(params['omega'], params['lead'], params['r_piston'])


def zf(t, params):
    
    """
    Function computing the float position depending on time and float parameters
    for initial conditions zf = 0 and vf = 0 at the beginning
    """
    
    return (params['u']*g*rho_w*t**3) / (6*params['m']*(1+params['a']))


def vf(t, params):
    
    """
    Function computing the float speed depending on time and float parameters
    for initial conditions zf = 0 and vf = 0 at the beginning
    """
    
    return (params['u']*g*rho_w*t**2) / (2*params['m']*(1+params['a']))


def tv(v, params):
    
    """
    Function computing the time necessary for the float to reach the speed v
    """
    
    return np.sqrt(2*v*params['m']*(1+params['a'])/(g*rho_w*params['u']))

def zv(v, params):
    
    """
    Function computing the distance necessary for the float to reach the speed v
    """
    
    return zf(tv(v,params),params)

if __name__ == '__main__':
    
    ''' Float position as a function of time, depending 
    on the added mass (a) and the piston flow u '''
    
    Omega = [12.4*2.*np.pi/360., 
             (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2,
             124.*2.*np.pi/360., 12.4*2.*np.pi/360., 
             (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2,
             124.*2.*np.pi/360., 12.4*2.*np.pi/360., 
             (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2,
             124.*2.*np.pi/360.]
    A = [1, 1, 1, 2, 2, 2, 0, 0, 0]
    
    
    t = np.linspace(0,10,100)
    fig, ax = plt.subplots()
    for o,a in zip(Omega,A):
        params['omega'] = o
        params['u'] = omega2dvdt(params['omega'], params['lead'], params['r_piston'])
        params['a'] = a
        if a == 1:
            color = 'green'
        elif a == 2:
            color = 'red'
        else: # a == 0
            color = 'black'
            
        if 12.4*2.*np.pi/360. - 0.01 <= o <= 12.4*2.*np.pi/360. + 0.01:
            k = 'k'
        elif (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2 - 0.01 <= o <= (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2 + 0.01:
            k = 'k--'
        else: # 124.*2.*np.pi/360. - 0.01 <= o <= 124.*2.*np.pi/360. + 0.01
            k = 'k:' 
        ax.plot(t, zf(t, params),k, c = color,
                label='a = {}, omega = {:.2e} rad.s^-1'.format(params['a'], o))
    
    plt.xlabel('Time (s)')
    plt.ylabel('Depth (m)')
    plt.title('Float position as a function of time')
    legend = ax.legend(loc='best', shadow=True, fontsize='medium')
    
    
    
    ''' Float speed as a function of time, depending
    on the added mass (a) and the piston flow u '''
    
    Omega = [12.4*2.*np.pi/360., 
             (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2,
             124.*2.*np.pi/360., 12.4*2.*np.pi/360., 
             (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2,
             124.*2.*np.pi/360., 12.4*2.*np.pi/360., 
             (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2,
             124.*2.*np.pi/360.]
    A = [1, 1, 1, 2, 2, 2, 0, 0, 0]
    
    
    t = np.linspace(0,10,100)
    fig, ax = plt.subplots()
    for o,a in zip(Omega,A):
        params['omega'] = o
        params['u'] = omega2dvdt(params['omega'], params['lead'], params['r_piston'])
        params['a'] = a
        if a == 1:
            color = 'green'
        elif a == 2:
            color = 'red'
        else: # a == 0
            color = 'black'
            
        if 12.4*2.*np.pi/360. - 0.01 <= o <= 12.4*2.*np.pi/360. + 0.01:
            k = 'k'
        elif (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2 - 0.01 <= o <= (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2 + 0.01:
            k = 'k--'
        else: # 124.*2.*np.pi/360. - 0.01 <= o <= 124.*2.*np.pi/360. + 0.01
            k = 'k:' 
        ax.plot(t, vf(t, params),k, c = color,
                label='a = {}, omega = {:.2e} rad.s^-1'.format(params['a'], o))
    
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Float velocity as a function of time')
    legend = ax.legend(loc='best', shadow=True, fontsize='medium')



    ''' Necessary time for the float to reach a given speed '''
    v = np.linspace(0, 0.1,200)
    
    Omega = [12.4*2.*np.pi/360., 
             (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2,
             124.*2.*np.pi/360., 12.4*2.*np.pi/360., 
             (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2,
             124.*2.*np.pi/360., 12.4*2.*np.pi/360., 
             (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2,
             124.*2.*np.pi/360.]
    A = [1, 1, 1, 2, 2, 2, 0, 0, 0]
    
    fig, ax = plt.subplots()
    for o,a in zip(Omega,A):
        params['omega'] = o
        params['u'] = omega2dvdt(params['omega'], params['lead'], params['r_piston'])
        params['a'] = a
        if a == 1:
            color = 'green'
        elif a == 2:
            color = 'red'
        else: # a == 0
            color = 'black'
            
        if 12.4*2.*np.pi/360. - 0.01 <= o <= 12.4*2.*np.pi/360. + 0.01:
            k = 'k'
        elif (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2 - 0.01 <= o <= (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2 + 0.01:
            k = 'k--'
        else: # 124.*2.*np.pi/360. - 0.01 <= o <= 124.*2.*np.pi/360. + 0.01
            k = 'k:' 
        ax.plot(v, tv(v, params),k, c = color,
                label='a = {}, omega = {:.2e} rad.s^-1'.format(params['a'], o))
        plt.xlabel('Given speed (m/s)')
        plt.ylabel('Necessary time (s)')
        plt.title('Necessary time for the float to reach a given speed with a = {} and u = {}'.format(params['a'], params['u']))
        legend = ax.legend(loc='best', shadow=True, fontsize='medium')
    
    
    
    ''' Necessary depth for the float to reach a given speed '''
    v = np.linspace(0, 0.1,200)
    
    Omega = [12.4*2.*np.pi/360., 
             (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2,
             124.*2.*np.pi/360., 12.4*2.*np.pi/360., 
             (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2,
             124.*2.*np.pi/360., 12.4*2.*np.pi/360., 
             (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2,
             124.*2.*np.pi/360.]
    A = [1, 1, 1, 2, 2, 2, 0, 0, 0]
    
    fig, ax = plt.subplots()
    for o,a in zip(Omega,A):
        params['omega'] = o
        params['u'] = omega2dvdt(params['omega'], params['lead'], params['r_piston'])
        params['a'] = a
        if a == 1:
            color = 'green'
        elif a == 2:
            color = 'red'
        else: # a == 0
            color = 'black'
            
        if 12.4*2.*np.pi/360. - 0.01 <= o <= 12.4*2.*np.pi/360. + 0.01:
            k = 'k'
        elif (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2 - 0.01 <= o <= (12.4*2.*np.pi/360. + 124.*2.*np.pi/360.)/2 + 0.01:
            k = 'k--'
        else: # 124.*2.*np.pi/360. - 0.01 <= o <= 124.*2.*np.pi/360. + 0.01
            k = 'k:' 
        ax.plot(v, zv(v, params),k, c = color,
                label='a = {}, omega = {:.2e} rad.s^-1'.format(params['a'], o))
        plt.xlabel('Given speed (m/s)')
        plt.ylabel('Necessary depth (m)')
        plt.title('Depth traveled before reaching a given speed with a = {} and u = {}'.format(params['a'], params['u']))
        legend = ax.legend(loc='best', shadow=True, fontsize='medium')