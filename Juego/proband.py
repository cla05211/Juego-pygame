 elif lista_teclas[pygame.K_z]:
                        if True in colisiones_mesas["choco_mesa"]:
                            toco_cliente = True         
                        for pedido in lista_pedidos:
                            if colision_barra and pedido.rect_objeto_izquierda and toco_cliente:
                                toco_cliente_con_comida = True
                                toco_cliente = False
                            elif colision_barra and pedido.rect_objeto_izquierda:
                                toco_comida_barra = True
            else:
                mantiene_presionado = False
                movimiento = [0,0]

            #Imagen mesa
            self.mesa.blitear_objeto(self.pantalla)
            self.mesa_dos.blitear_objeto(self.pantalla)
            print(toco_cliente)
            #determinar posicion y blitear comida
            for mesa in lista_mesas:   
                if toco_cliente and not llevando_comida and not mesa.mesa_atendida:
                    toco_cliente = False
                    lista_pedidos = manejar_lista_pedidos(lista_pedidos,"agregar",Comidas(self.diccionario_imagenes["hamburguesa"],self.rect_fuera_pantalla,self.jugador.rect_personaje,mesa.rect_objeto))
                for pedido in lista_pedidos:
                    if not mesa.mesa_atendida:
                        print("barra")
                        mesa.actualizar_estado_mesa(True)
                        llevando_comida = False
                        toco_cliente = False
                        pedido.determinar_posicion_comida("barra",lista_pedidos)
                    elif toco_comida_barra:
                        pedido.determinar_posicion_comida("personaje",lista_pedidos)
                    if toco_cliente_con_comida:
                        print("mesa")
                        toco_comida_barra = False
                        pedido.determinar_posicion_comida("mesa",lista_pedidos)