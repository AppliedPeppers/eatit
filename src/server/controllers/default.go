package controllers

import (
	"github.com/astaxie/beego"
)

type MainController struct {
	beego.Controller
}

type Card struct {
	Title string
	Text string
}

func (c *MainController) Get() {
	var cards []Card
	s := Card{
		Title: "А1",
		Text: "Ингридиенты для А1",
	}
	cards = append(cards, s)
	s = Card{
		Title: "А2",
		Text: "Ингридиенты для А2",
	}
	cards = append(cards, s)
	s = Card{
		Title: "А3",
		Text: "Ингридиенты для А3",
	}
	cards = append(cards, s)
	c.Data["cards"] = cards
	c.TplName = "index.tpl"
}
