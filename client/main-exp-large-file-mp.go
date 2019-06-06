package main

import (
	"bytes"
	"crypto/tls"
	"fmt"
	quic "github.com/lucas-clemente/quic-go"
	"github.com/lucas-clemente/quic-go/h2quic"
	"io"
	"net/http"
	"time"
)

func main() {
	quicConfig := &quic.Config{
		//	CacheHandshake: true,
		CreatePaths: true,
	}

	client := http.Client{
		Transport: &h2quic.RoundTripper{
			QuicConfig: quicConfig,
			TLSClientConfig: &tls.Config{
				InsecureSkipVerify: true,
			},
		},
	}

	start := time.Now()
	req, err := http.NewRequest("GET", "https://10.0.0.1:9301/random-bin", nil)
	// req.Host = "server.quic.isel.lab"

	if err != nil {
		panic(err.Error())
	}

	res, err := client.Do(req)

	if err != nil {
		panic(err.Error())
	} else {
		buf := &bytes.Buffer{}
		io.Copy(buf, res.Body)
		elapsed := time.Since(start)

		fmt.Printf("LARGE FILE TOOK %s", elapsed)

		fmt.Println()

	}
}
