# UT4-TE1: Funciones

### TAREA EVALUABLE

![Vending machine](./images/vending-machine.svg)

## Objetivo

Escriba un programa en Python que permita simular el comportamiento de una **MÁQUINA DE VENDING**.

## Datos de entrada

`operations.dat`

| Código | Descripción                                                    | Argumentos                                                                | Ejemplo      | Condiciones de error                                                                                                                                                  |
| ------ | -------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `O`    | Hacer un pedido <br>(**O**rder)                                | - Código del producto.<br>- Cantidad solicitada.<br>- Dinero introducido. | `O F19 4 10` | - E1: El código del producto no existe.<br>- E2: No hay stock suficiente del producto solicitado.<br>- E3: El importe total introducido no cubre el total del pedido. |
| `R`    | Reponer un producto\* <br>(**R**estock product)                | - Código del producto.<br>- Cantidad repuesta.                            | `R D12 7`    |
| `P`    | Cambiar el precio de un producto<br>(change product **P**rice) | - Código del producto.<br>- Nuevo precio del producto.                    | `P F10 3`    | - E1: El código del producto no existe.                                                                                                                               |
| `M`    | Reponer dinero <br>(restock **M**oney)                         | - Cantidad de dinero.                                                     | `M 20`       |

\* Si el producto no existe, se debe añadir un nuevo producto con la cantidad indicada y precio 0€.

**Códigos de error:**

| Código | Error                 |
| ------ | --------------------- |
| E1     | PRODUCT NOT FOUND     |
| E2     | UNAVAILABLE STOCK     |
| E3     | NOT ENOUGH USER MONEY |

## Datos de salida

`status.dat`

Este fichero contendrá la situación de la máquina de vending después de aplicar las operaciones ~~indicadas~~ correctas del fichero `operations.dat`. Es decir, este fichero deberá contener las monedas de la máquina y las características de cada producto existente.

En la primera línea debe aparecer el saldo actual de la máquina y a partir de la segunda línea todos los productos **ordenados por su código** indicando cantidad en stock y precio unitario.

Por ejemplo:

```
99
D12 47 1
D31 16 5
F10 24 2
F19 29 3
```

#### OPCIONAL 👇

A efectos de depuración, puede ayudar el hecho de **mostrar por pantalla** el resultado de cada operación de entrada indicando si se ha realizado con éxito o no.

Por ejemplo:

```
✅ O F19 4 10
✅ R D12 7
❌ P F10 3 (E3: PRODUCT NOT FOUND)
✅ M 20
```

> 💡 En el caso de que una operación de un error, se podría incluir el código del error (entre paréntesis).

## Condiciones de error

Para cada operación hay que tener en cuenta que se puede producir alguna condición de error tal y como se especifica en la tabla de operaciones.

Si una operación produce un error, se cancelará dicha operación pero se seguirá tratando el resto de operaciones pendientes.

## Notas

-   Se puede asumir que todos los precios y cantidades serán valores enteros mayores o iguales que 0.
-   Crear todas las funciones que se consideren necesarias.
-   Agregar anotaciones de tipos en las funciones.
-   No es necesario añadir "docstrings" al código.
-   Utilizar sólo herramientas de Python que se hayan visto hasta el momento en clase.
-   No utilizar `input()` en el código final: trabajar únicamente con ficheros.
