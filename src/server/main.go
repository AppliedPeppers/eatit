package main

import (
	_ "server/routers"
	"github.com/astaxie/beego"
)

func main() {
	/*beego.SetStaticPath("/", "static/")*/
	beego.SetStaticPath("/css/", "static/css/")
	beego.SetStaticPath("/js/", "static/js/")
	beego.Run()
}

