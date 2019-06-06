package main

import (
	"bytes"
	"crypto/tls"
	"fmt"
	"github.com/lucas-clemente/quic-go/h2quic"
	"io"
	"net/http"
	"time"
)

func main() {
	client := http.Client{
		Transport: &h2quic.RoundTripper{
			TLSClientConfig: &tls.Config{
				InsecureSkipVerify: true,
			},
		},
	}

	start := time.Now()
	for i := 0; i < 200; i++ {
		req, err := http.NewRequest("GET", "https://10.0.0.1:9301/random-num", nil)
		// req.Host = "server.quic.isel.lab"

		if err != nil {
			panic(err.Error())
		}

		res, err2 := client.Do(req)
		if err2 != nil {
			panic(err.Error())
		}
		buf := &bytes.Buffer{}
		io.Copy(buf, res.Body)
	}
	elapsed := time.Since(start)

	fmt.Printf("SMALL REQUESTS TOOK %s", elapsed)
	fmt.Println()
}
