# Suma

```
fun suma(n:int)
{
  if(n==0)
  {
    return
  }
  else
  {
    return n+suma(n-1)
  }
}

fun main()
{
  println(suma(5))
}
```
