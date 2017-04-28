@echo off
set GOPATH=%cd%

go get github.com/astaxie/beego && ^
go get github.com/beego/bee && ^
echo "Install OK"