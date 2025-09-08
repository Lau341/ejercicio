# KOTLIN (P.O.O)

## Función
```
fun saludar()
{
  print("Hola")
}
saludar()
```

## Clase
```
class persona(val nombre : String , var edad : int)
{
  fun saludar(){
    print("Hola")
  }
}
val persona = Persona("Ana" , 25)
persona saludar()
```

## Función main
```
fun main()
{
  val persona = Persona("Ana" , 25)
  Persona.saludar()
}
```

## Acceso
```
- *private*: Se accede a los atributos con setters y getters
- *public*: Se puede acceder directamente desde el objeto disponible para la clase
```
## Herencia
```
open class Animal
{
}
class Perro: Animal()
{
}
```
## Setter
```
fun setRaza(nomR : String)
{
  raza = nomR
}
```
## Getter
```
fun getRaza() : String
{
  return raza
}
obj.set Raza("Caniche")
```
## Polimorfismo
```
open class Animal
{
  open fun hacerSonido()
  {
    println("Guau")
  }
}
```
