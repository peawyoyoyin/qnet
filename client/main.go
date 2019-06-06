package main

import (
	"bytes"
	"crypto/tls"
	"fmt"
	"github.com/lucas-clemente/quic-go/h2quic"
	"io"
	"net/http"
)

func main() {
	client := http.Client{
		Transport: &h2quic.RoundTripper{
			TLSClientConfig: &tls.Config{
				InsecureSkipVerify: true,
			},
		},
	}

	req, err := http.NewRequest("GET", "https://10.0.0.1:9301/files/random-bin", nil)
	// req.Host = "server.quic.isel.lab"

	if err != nil {
		panic(err.Error())
	}

	res, err := client.Do(req)

	// res, err := client.Get("https://localhost:9301/hello")

	if err != nil {
		panic(err.Error())
	} else {
		buf := &bytes.Buffer{}
		io.Copy(buf, res.Body)
		// fmt.Printf("%s", buf.Bytes())
		fmt.Println("Response finished")
	}
}
