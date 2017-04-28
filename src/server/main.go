package main

import (
	_ "server/routers"
	"github.com/astaxie/beego"
)

func main() {
	beego.SetStaticPath("/", "static")
	beego.Run()
}

