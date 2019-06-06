package main

import (
//	"bytes"
	"crypto/tls"
	"fmt"
	quic "github.com/lucas-clemente/quic-go"
	"github.com/lucas-clemente/quic-go/h2quic"
//	"io"
	"net/http"
)

func main() {
	quicConfig := &quic.Config{
		//	CacheHandshake: true,
		CreatePaths:      true,
		// FixedNumberPaths: 4,
	}
	// fmt.Printf("AT CODE FixedNumberPaths: %d\n", quicConfig.FixedNumberPaths)
	client := http.Client{
		Transport: &h2quic.RoundTripper{
			QuicConfig: quicConfig,
			TLSClientConfig: &tls.Config{
				InsecureSkipVerify: true,
			},
		},
	}

	req, err := http.NewRequest("GET", "https://10.0.0.1:9301/random-bin", nil)
	// req.Host = "server.quic.isel.lab"

	if err != nil {
		panic(err.Error())
	}

	_, err = client.Do(req)

	// res, err := client.Get("https://localhost:9301/hello")

	if err != nil {
		panic(err.Error())
	} else {
		buf := &bytes.Buffer{}
		io.Copy(buf, res.Body)
		// fmt.Printf("%s", buf.Bytes())
		fmt.Printf("request completed")
		fmt.Println()
	}
}
