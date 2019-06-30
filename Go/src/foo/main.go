package main
import "fmt"
import "math"

const s string = "constant"

func main() {
	sum := 0
	for i := 0; i < 10; i = i + 1 {
		fmt.Println("I: ",i)
	}
	fmt.Println(sum)


	for i := 0; i < 5; i++ {
	println("abc", i)
	println("juchuu")
	}

	fmt.Println("go" + "lang")
    fmt.Println("1+1 =", 1+1)
    fmt.Println("7.0/3.0 =", 7.0/3.0)
    fmt.Println(true && false)
    fmt.Println(true || false)
    fmt.Println(!true)


	var a = "initial"
    fmt.Println(a)

	// You can declare multiple variables at once.
    var b, c int = 1, 2
    fmt.Println(b, c)

	// Go will infer the type of initialized variables.
    var d = true
    fmt.Println(d)

	// Variables declared without a corresponding initialization are zero-valued. For example, the zero value for an int is 0.
    var e int
    fmt.Println(e)

	// The := syntax is shorthand for declaring and initializing a variable, e.g. for var f string = "short" in this case.
    f := "short"
	fmt.Println(f)
	
	fmt.Println(s)

	//	A const statement can appear anywhere a var statement can.
	const n = 500000000
	
	// Constant expressions perform arithmetic with arbitrary precision.
	const d = 3e20 / n
	fmt.Println(d)

	// A numeric constant has no type until it’s given one, such as by an explicit cast.
	fmt.Println(int64(d))

	//	A number can be given a type by using it in a context that requires one, such as a variable assignment or function call. For example, here math.Sin expects a float64.
	fmt.Println(math.Sin(n))

}



