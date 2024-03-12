lockfileVersion: '6.0'

dependencies:
  '@fortawesome/fontawesome-svg-core':
    specifier: ^6.4.0
    version: 6.4.0
  '@fortawesome/free-brands-svg-icons':
    specifier: ^6.4.0
    version: 6.4.0
  '@fortawesome/free-regular-svg-icons':
    specifier: ^6.4.0
    version: 6.4.0
  '@fortawesome/free-solid-svg-icons':
    specifier: ^6.4.0
    version: 6.4.0
  '@fortawesome/react-fontawesome':
    specifier: ^0.2.0
    version: 0.2.0(@fortawesome/fontawesome-svg-core@6.4.0)(react@18.2.0)
  '@headlessui/react':
    specifier: ^1.7.15
    version: 1.7.15(react-dom@18.2.0)(react@18.2.0)
  '@rainbow-me/rainbowkit':
    specifier: ^1.0.7
    version: 1.0.7(@types/react@18.0.37)(react-dom@18.2.0)(react@18.2.0)(viem@1.4.1)(wagmi@1.3.9)
  '@types/p5':
    specifier: ^1.6.2
    version: 1.6.2
  animated-number-react:
    specifier: ^0.1.2
    version: 0.1.2(react-dom@18.2.0)(react@18.2.0)
  lottie-react:
    specifier: ^2.4.0
    version: 2.4.0(react-dom@18.2.0)(react@18.2.0)
  p5:
    specifier: ^1.6.0
    version: 1.6.0
  react:
    specifier: ^18.2.0
    version: 18.2.0
  react-dom:
    specifier: ^18.2.0
    version: 18.2.0(react@18.2.0)
  react-intersection-observer:
    specifier: ^9.4.4
    version: 9.4.4(react@18.2.0)
  vanta:
    specifier: ^0.5.24
    version: 0.5.24
  viem:
    specifier: ^1.4.1
    version: 1.4.1(typescript@5.0.2)
  wagmi:
    specifier: ^1.3.9
    version: 1.3.9(react-dom@18.2.0)(react@18.2.0)(typescript@5.0.2)(viem@1.4.1)

devDependencies:
  '@types/react':
    specifier: ^18.0.37
    version: 18.0.37
  '@types/react-dom':
    specifier: ^18.0.11
    version: 18.0.11
  '@typescript-eslint/eslint-plugin':
    specifier: ^5.59.0
    version: 5.59.0(@typescript-eslint/parser@5.59.0)(eslint@8.38.0)(typescript@5.0.2)
  '@typescript-eslint/parser':
    specifier: ^5.59.0
    version: 5.59.0(eslint@8.38.0)(typescript@5.0.2)
  '@vitejs/plugin-react':
    specifier: ^4.0.0
    version: 4.0.0(vite@4.3.9)
  eslint:
    specifier: ^8.38.0
    version: 8.38.0
  eslint-plugin-react-hooks:
    specifier: ^4.6.0
    version: 4.6.0(eslint@8.38.0)
  eslint-plugin-react-refresh:
    specifier: ^0.3.4
    version: 0.3.4(eslint@8.38.0)
  prettier:
    specifier: ^2.8.8
    version: 2.8.8
  sass:
    specifier: ^1.63.2
    version: 1.63.2
  typescript:
    specifier: ^5.0.2
    version: 5.0.2
  vite:
    specifier: ^4.3.9
    version: 4.3.9(sass@1.63.2)

packages:

  /@adraffy/ens-normalize@1.9.0:
    resolution: {integrity: sha512-iowxq3U30sghZotgl4s/oJRci6WPBfNO5YYgk2cIOMCHr3LeGPcsZjCEr+33Q4N+oV3OABDAtA+pyvWjbvBifQ==}
    dev: false

  /@ampproject/remapping@2.2.1:
    resolution: {integrity: sha512-lFMjJTrFL3j7L9yBxwYfCq2k6qqwHyzuUl/XBnif78PWTJYyL/dfowQHWE3sp6U6ZzqWiiIZnpTMO96zhkjwtg==}
    engines: {node: '>=6.0.0'}
    dependencies:
      '@jridgewell/gen-mapping': 0.3.3
      '@jridgewell/trace-mapping': 0.3.18
    dev: true

  /@babel/code-frame@7.21.4:
    resolution: {integrity: sha512-LYvhNKfwWSPpocw8GI7gpK2nq3HSDuEPC/uSYaALSJu9xjsalaaYFOq0Pwt5KmVqwEbZlDu81aLXwBOmD/Fv9g==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/highlight': 7.18.6
    dev: true

  /@babel/compat-data@7.22.3:
    resolution: {integrity: sha512-aNtko9OPOwVESUFp3MZfD8Uzxl7JzSeJpd7npIoxCasU37PFbAQRpKglkaKwlHOyeJdrREpo8TW8ldrkYWwvIQ==}
    engines: {node: '>=6.9.0'}
    dev: true

  /@babel/core@7.22.1:
    resolution: {integrity: sha512-Hkqu7J4ynysSXxmAahpN1jjRwVJ+NdpraFLIWflgjpVob3KNyK3/tIUc7Q7szed8WMp0JNa7Qtd1E9Oo22F9gA==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@ampproject/remapping': 2.2.1
      '@babel/code-frame': 7.21.4
      '@babel/generator': 7.22.3
      '@babel/helper-compilation-targets': 7.22.1(@babel/core@7.22.1)
      '@babel/helper-module-transforms': 7.22.1
      '@babel/helpers': 7.22.3
      '@babel/parser': 7.22.4
      '@babel/template': 7.21.9
      '@babel/traverse': 7.22.4
      '@babel/types': 7.22.4
      convert-source-map: 1.9.0
      debug: 4.3.4
      gensync: 1.0.0-beta.2
      json5: 2.2.3
      semver: 6.3.0
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@babel/generator@7.22.3:
    resolution: {integrity: sha512-C17MW4wlk//ES/CJDL51kPNwl+qiBQyN7b9SKyVp11BLGFeSPoVaHrv+MNt8jwQFhQWowW88z1eeBx3pFz9v8A==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/types': 7.22.4
      '@jridgewell/gen-mapping': 0.3.3
      '@jridgewell/trace-mapping': 0.3.18
      jsesc: 2.5.2
    dev: true

  /@babel/helper-compilation-targets@7.22.1(@babel/core@7.22.1):
    resolution: {integrity: sha512-Rqx13UM3yVB5q0D/KwQ8+SPfX/+Rnsy1Lw1k/UwOC4KC6qrzIQoY3lYnBu5EHKBlEHHcj0M0W8ltPSkD8rqfsQ==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0
    dependencies:
      '@babel/compat-data': 7.22.3
      '@babel/core': 7.22.1
      '@babel/helper-validator-option': 7.21.0
      browserslist: 4.21.7
      lru-cache: 5.1.1
      semver: 6.3.0
    dev: true

  /@babel/helper-environment-visitor@7.22.1:
    resolution: {integrity: sha512-Z2tgopurB/kTbidvzeBrc2To3PUP/9i5MUe+fU6QJCQDyPwSH2oRapkLw3KGECDYSjhQZCNxEvNvZlLw8JjGwA==}
    engines: {node: '>=6.9.0'}
    dev: true

  /@babel/helper-function-name@7.21.0:
    resolution: {integrity: sha512-HfK1aMRanKHpxemaY2gqBmL04iAPOPRj7DxtNbiDOrJK+gdwkiNRVpCpUJYbUT+aZyemKN8brqTOxzCaG6ExRg==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/template': 7.21.9
      '@babel/types': 7.22.4
    dev: true

  /@babel/helper-hoist-variables@7.18.6:
    resolution: {integrity: sha512-UlJQPkFqFULIcyW5sbzgbkxn2FKRgwWiRexcuaR8RNJRy8+LLveqPjwZV/bwrLZCN0eUHD/x8D0heK1ozuoo6Q==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/types': 7.22.4
    dev: true

  /@babel/helper-module-imports@7.21.4:
    resolution: {integrity: sha512-orajc5T2PsRYUN3ZryCEFeMDYwyw09c/pZeaQEZPH0MpKzSvn3e0uXsDBu3k03VI+9DBiRo+l22BfKTpKwa/Wg==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/types': 7.22.4
    dev: true

  /@babel/helper-module-transforms@7.22.1:
    resolution: {integrity: sha512-dxAe9E7ySDGbQdCVOY/4+UcD8M9ZFqZcZhSPsPacvCG4M+9lwtDDQfI2EoaSvmf7W/8yCBkGU0m7Pvt1ru3UZw==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/helper-environment-visitor': 7.22.1
      '@babel/helper-module-imports': 7.21.4
      '@babel/helper-simple-access': 7.21.5
      '@babel/helper-split-export-declaration': 7.18.6
      '@babel/helper-validator-identifier': 7.19.1
      '@babel/template': 7.21.9
      '@babel/traverse': 7.22.4
      '@babel/types': 7.22.4
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@babel/helper-plugin-utils@7.21.5:
    resolution: {integrity: sha512-0WDaIlXKOX/3KfBK/dwP1oQGiPh6rjMkT7HIRv7i5RR2VUMwrx5ZL0dwBkKx7+SW1zwNdgjHd34IMk5ZjTeHVg==}
    engines: {node: '>=6.9.0'}
    dev: true

  /@babel/helper-simple-access@7.21.5:
    resolution: {integrity: sha512-ENPDAMC1wAjR0uaCUwliBdiSl1KBJAVnMTzXqi64c2MG8MPR6ii4qf7bSXDqSFbr4W6W028/rf5ivoHop5/mkg==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/types': 7.22.4
    dev: true

  /@babel/helper-split-export-declaration@7.18.6:
    resolution: {integrity: sha512-bde1etTx6ZyTmobl9LLMMQsaizFVZrquTEHOqKeQESMKo4PlObf+8+JA25ZsIpZhT/WEd39+vOdLXAFG/nELpA==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/types': 7.22.4
    dev: true

  /@babel/helper-string-parser@7.21.5:
    resolution: {integrity: sha512-5pTUx3hAJaZIdW99sJ6ZUUgWq/Y+Hja7TowEnLNMm1VivRgZQL3vpBY3qUACVsvw+yQU6+YgfBVmcbLaZtrA1w==}
    engines: {node: '>=6.9.0'}
    dev: true

  /@babel/helper-validator-identifier@7.19.1:
    resolution: {integrity: sha512-awrNfaMtnHUr653GgGEs++LlAvW6w+DcPrOliSMXWCKo597CwL5Acf/wWdNkf/tfEQE3mjkeD1YOVZOUV/od1w==}
    engines: {node: '>=6.9.0'}
    dev: true

  /@babel/helper-validator-option@7.21.0:
    resolution: {integrity: sha512-rmL/B8/f0mKS2baE9ZpyTcTavvEuWhTTW8amjzXNvYG4AwBsqTLikfXsEofsJEfKHf+HQVQbFOHy6o+4cnC/fQ==}
    engines: {node: '>=6.9.0'}
    dev: true

  /@babel/helpers@7.22.3:
    resolution: {integrity: sha512-jBJ7jWblbgr7r6wYZHMdIqKc73ycaTcCaWRq4/2LpuPHcx7xMlZvpGQkOYc9HeSjn6rcx15CPlgVcBtZ4WZJ2w==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/template': 7.21.9
      '@babel/traverse': 7.22.4
      '@babel/types': 7.22.4
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@babel/highlight@7.18.6:
    resolution: {integrity: sha512-u7stbOuYjaPezCuLj29hNW1v64M2Md2qupEKP1fHc7WdOA3DgLh37suiSrZYY7haUB7iBeQZ9P1uiRF359do3g==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/helper-validator-identifier': 7.19.1
      chalk: 2.4.2
      js-tokens: 4.0.0
    dev: true

  /@babel/parser@7.22.4:
    resolution: {integrity: sha512-VLLsx06XkEYqBtE5YGPwfSGwfrjnyPP5oiGty3S8pQLFDFLaS8VwWSIxkTXpcvr5zeYLE6+MBNl2npl/YnfofA==}
    engines: {node: '>=6.0.0'}
    hasBin: true
    dependencies:
      '@babel/types': 7.22.4
    dev: true

  /@babel/plugin-transform-react-jsx-self@7.21.0(@babel/core@7.22.1):
    resolution: {integrity: sha512-f/Eq+79JEu+KUANFks9UZCcvydOOGMgF7jBrcwjHa5jTZD8JivnhCJYvmlhR/WTXBWonDExPoW0eO/CR4QJirA==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0-0
    dependencies:
      '@babel/core': 7.22.1
      '@babel/helper-plugin-utils': 7.21.5
    dev: true

  /@babel/plugin-transform-react-jsx-source@7.19.6(@babel/core@7.22.1):
    resolution: {integrity: sha512-RpAi004QyMNisst/pvSanoRdJ4q+jMCWyk9zdw/CyLB9j8RXEahodR6l2GyttDRyEVWZtbN+TpLiHJ3t34LbsQ==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0-0
    dependencies:
      '@babel/core': 7.22.1
      '@babel/helper-plugin-utils': 7.21.5
    dev: true

  /@babel/runtime@7.22.6:
    resolution: {integrity: sha512-wDb5pWm4WDdF6LFUde3Jl8WzPA+3ZbxYqkC6xAXuD3irdEHN1k0NfTRrJD8ZD378SJ61miMLCqIOXYhd8x+AJQ==}
    engines: {node: '>=6.9.0'}
    dependencies:
      regenerator-runtime: 0.13.11
    dev: false

  /@babel/template@7.21.9:
    resolution: {integrity: sha512-MK0X5k8NKOuWRamiEfc3KEJiHMTkGZNUjzMipqCGDDc6ijRl/B7RGSKVGncu4Ro/HdyzzY6cmoXuKI2Gffk7vQ==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/code-frame': 7.21.4
      '@babel/parser': 7.22.4
      '@babel/types': 7.22.4
    dev: true

  /@babel/traverse@7.22.4:
    resolution: {integrity: sha512-Tn1pDsjIcI+JcLKq1AVlZEr4226gpuAQTsLMorsYg9tuS/kG7nuwwJ4AB8jfQuEgb/COBwR/DqJxmoiYFu5/rQ==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/code-frame': 7.21.4
      '@babel/generator': 7.22.3
      '@babel/helper-environment-visitor': 7.22.1
      '@babel/helper-function-name': 7.21.0
      '@babel/helper-hoist-variables': 7.18.6
      '@babel/helper-split-export-declaration': 7.18.6
      '@babel/parser': 7.22.4
      '@babel/types': 7.22.4
      debug: 4.3.4
      globals: 11.12.0
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@babel/types@7.22.4:
    resolution: {integrity: sha512-Tx9x3UBHTTsMSW85WB2kphxYQVvrZ/t1FxD88IpSgIjiUJlCm9z+xWIDwyo1vffTwSqteqyznB8ZE9vYYk16zA==}
    engines: {node: '>=6.9.0'}
    dependencies:
      '@babel/helper-string-parser': 7.21.5
      '@babel/helper-validator-identifier': 7.19.1
      to-fast-properties: 2.0.0
    dev: true

  /@coinbase/wallet-sdk@3.7.1:
    resolution: {integrity: sha512-LjyoDCB+7p0waQXfK+fUgcAs3Ezk6S6e+LYaoFjpJ6c9VTop3NyZF40Pi7df4z7QJohCwzuIDjz0Rhtig6Y7Pg==}
    engines: {node: '>= 10.0.0'}
    dependencies:
      '@metamask/safe-event-emitter': 2.0.0
      '@solana/web3.js': 1.78.0
      bind-decorator: 1.0.11
      bn.js: 5.2.1
      buffer: 6.0.3
      clsx: 1.2.1
      eth-block-tracker: 6.1.0
      eth-json-rpc-filters: 5.1.0
      eth-rpc-errors: 4.0.2
      json-rpc-engine: 6.1.0
      keccak: 3.0.3
      preact: 10.16.0
      qs: 6.11.2
      rxjs: 6.6.7
      sha.js: 2.4.11
      stream-browserify: 3.0.0
      util: 0.12.5
    transitivePeerDependencies:
      - bufferutil
      - encoding
      - supports-color
      - utf-8-validate
    dev: false

  /@emotion/hash@0.8.0:
    resolution: {integrity: sha512-kBJtf7PH6aWwZ6fka3zQ0p6SBYzx4fl1LoZXE2RrnYST9Xljm7WfKJrU4g/Xr3Beg72MLrp1AWNUmuYJTL7Cow==}
    dev: false

  /@esbuild/android-arm64@0.17.19:
    resolution: {integrity: sha512-KBMWvEZooR7+kzY0BtbTQn0OAYY7CsiydT63pVEaPtVYF0hXbUaOyZog37DKxK7NF3XacBJOpYT4adIJh+avxA==}
    engines: {node: '>=12'}
    cpu: [arm64]
    os: [android]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/android-arm@0.17.19:
    resolution: {integrity: sha512-rIKddzqhmav7MSmoFCmDIb6e2W57geRsM94gV2l38fzhXMwq7hZoClug9USI2pFRGL06f4IOPHHpFNOkWieR8A==}
    engines: {node: '>=12'}
    cpu: [arm]
    os: [android]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/android-x64@0.17.19:
    resolution: {integrity: sha512-uUTTc4xGNDT7YSArp/zbtmbhO0uEEK9/ETW29Wk1thYUJBz3IVnvgEiEwEa9IeLyvnpKrWK64Utw2bgUmDveww==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [android]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/darwin-arm64@0.17.19:
    resolution: {integrity: sha512-80wEoCfF/hFKM6WE1FyBHc9SfUblloAWx6FJkFWTWiCoht9Mc0ARGEM47e67W9rI09YoUxJL68WHfDRYEAvOhg==}
    engines: {node: '>=12'}
    cpu: [arm64]
    os: [darwin]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/darwin-x64@0.17.19:
    resolution: {integrity: sha512-IJM4JJsLhRYr9xdtLytPLSH9k/oxR3boaUIYiHkAawtwNOXKE8KoU8tMvryogdcT8AU+Bflmh81Xn6Q0vTZbQw==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [darwin]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/freebsd-arm64@0.17.19:
    resolution: {integrity: sha512-pBwbc7DufluUeGdjSU5Si+P3SoMF5DQ/F/UmTSb8HXO80ZEAJmrykPyzo1IfNbAoaqw48YRpv8shwd1NoI0jcQ==}
    engines: {node: '>=12'}
    cpu: [arm64]
    os: [freebsd]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/freebsd-x64@0.17.19:
    resolution: {integrity: sha512-4lu+n8Wk0XlajEhbEffdy2xy53dpR06SlzvhGByyg36qJw6Kpfk7cp45DR/62aPH9mtJRmIyrXAS5UWBrJT6TQ==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [freebsd]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/linux-arm64@0.17.19:
    resolution: {integrity: sha512-ct1Tg3WGwd3P+oZYqic+YZF4snNl2bsnMKRkb3ozHmnM0dGWuxcPTTntAF6bOP0Sp4x0PjSF+4uHQ1xvxfRKqg==}
    engines: {node: '>=12'}
    cpu: [arm64]
    os: [linux]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/linux-arm@0.17.19:
    resolution: {integrity: sha512-cdmT3KxjlOQ/gZ2cjfrQOtmhG4HJs6hhvm3mWSRDPtZ/lP5oe8FWceS10JaSJC13GBd4eH/haHnqf7hhGNLerA==}
    engines: {node: '>=12'}
    cpu: [arm]
    os: [linux]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/linux-ia32@0.17.19:
    resolution: {integrity: sha512-w4IRhSy1VbsNxHRQpeGCHEmibqdTUx61Vc38APcsRbuVgK0OPEnQ0YD39Brymn96mOx48Y2laBQGqgZ0j9w6SQ==}
    engines: {node: '>=12'}
    cpu: [ia32]
    os: [linux]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/linux-loong64@0.17.19:
    resolution: {integrity: sha512-2iAngUbBPMq439a+z//gE+9WBldoMp1s5GWsUSgqHLzLJ9WoZLZhpwWuym0u0u/4XmZ3gpHmzV84PonE+9IIdQ==}
    engines: {node: '>=12'}
    cpu: [loong64]
    os: [linux]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/linux-mips64el@0.17.19:
    resolution: {integrity: sha512-LKJltc4LVdMKHsrFe4MGNPp0hqDFA1Wpt3jE1gEyM3nKUvOiO//9PheZZHfYRfYl6AwdTH4aTcXSqBerX0ml4A==}
    engines: {node: '>=12'}
    cpu: [mips64el]
    os: [linux]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/linux-ppc64@0.17.19:
    resolution: {integrity: sha512-/c/DGybs95WXNS8y3Ti/ytqETiW7EU44MEKuCAcpPto3YjQbyK3IQVKfF6nbghD7EcLUGl0NbiL5Rt5DMhn5tg==}
    engines: {node: '>=12'}
    cpu: [ppc64]
    os: [linux]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/linux-riscv64@0.17.19:
    resolution: {integrity: sha512-FC3nUAWhvFoutlhAkgHf8f5HwFWUL6bYdvLc/TTuxKlvLi3+pPzdZiFKSWz/PF30TB1K19SuCxDTI5KcqASJqA==}
    engines: {node: '>=12'}
    cpu: [riscv64]
    os: [linux]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/linux-s390x@0.17.19:
    resolution: {integrity: sha512-IbFsFbxMWLuKEbH+7sTkKzL6NJmG2vRyy6K7JJo55w+8xDk7RElYn6xvXtDW8HCfoKBFK69f3pgBJSUSQPr+4Q==}
    engines: {node: '>=12'}
    cpu: [s390x]
    os: [linux]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/linux-x64@0.17.19:
    resolution: {integrity: sha512-68ngA9lg2H6zkZcyp22tsVt38mlhWde8l3eJLWkyLrp4HwMUr3c1s/M2t7+kHIhvMjglIBrFpncX1SzMckomGw==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [linux]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/netbsd-x64@0.17.19:
    resolution: {integrity: sha512-CwFq42rXCR8TYIjIfpXCbRX0rp1jo6cPIUPSaWwzbVI4aOfX96OXY8M6KNmtPcg7QjYeDmN+DD0Wp3LaBOLf4Q==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [netbsd]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/openbsd-x64@0.17.19:
    resolution: {integrity: sha512-cnq5brJYrSZ2CF6c35eCmviIN3k3RczmHz8eYaVlNasVqsNY+JKohZU5MKmaOI+KkllCdzOKKdPs762VCPC20g==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [openbsd]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/sunos-x64@0.17.19:
    resolution: {integrity: sha512-vCRT7yP3zX+bKWFeP/zdS6SqdWB8OIpaRq/mbXQxTGHnIxspRtigpkUcDMlSCOejlHowLqII7K2JKevwyRP2rg==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [sunos]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/win32-arm64@0.17.19:
    resolution: {integrity: sha512-yYx+8jwowUstVdorcMdNlzklLYhPxjniHWFKgRqH7IFlUEa0Umu3KuYplf1HUZZ422e3NU9F4LGb+4O0Kdcaag==}
    engines: {node: '>=12'}
    cpu: [arm64]
    os: [win32]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/win32-ia32@0.17.19:
    resolution: {integrity: sha512-eggDKanJszUtCdlVs0RB+h35wNlb5v4TWEkq4vZcmVt5u/HiDZrTXe2bWFQUez3RgNHwx/x4sk5++4NSSicKkw==}
    engines: {node: '>=12'}
    cpu: [ia32]
    os: [win32]
    requiresBuild: true
    dev: true
    optional: true

  /@esbuild/win32-x64@0.17.19:
    resolution: {integrity: sha512-lAhycmKnVOuRYNtRtatQR1LPQf2oYCkRGkSFnseDAKPl8lu5SOsK/e1sXe5a0Pc5kHIHe6P2I/ilntNv2xf3cA==}
    engines: {node: '>=12'}
    cpu: [x64]
    os: [win32]
    requiresBuild: true
    dev: true
    optional: true

  /@eslint-community/eslint-utils@4.4.0(eslint@8.38.0):
    resolution: {integrity: sha512-1/sA4dwrzBAyeUoQ6oxahHKmrZvsnLCg4RfxW3ZFGGmQkSNQPFNLV9CUEFQP1x9EYXHTo5p6xdhZM1Ne9p/AfA==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    peerDependencies:
      eslint: ^6.0.0 || ^7.0.0 || >=8.0.0
    dependencies:
      eslint: 8.38.0
      eslint-visitor-keys: 3.4.1
    dev: true

  /@eslint-community/regexpp@4.5.1:
    resolution: {integrity: sha512-Z5ba73P98O1KUYCCJTUeVpja9RcGoMdncZ6T49FCUl2lN38JtCJ+3WgIDBv0AuY4WChU5PmtJmOCTlN6FZTFKQ==}
    engines: {node: ^12.0.0 || ^14.0.0 || >=16.0.0}
    dev: true

  /@eslint/eslintrc@2.0.3:
    resolution: {integrity: sha512-+5gy6OQfk+xx3q0d6jGZZC3f3KzAkXc/IanVxd1is/VIIziRqqt3ongQz0FiTUXqTk0c7aDB3OaFuKnuSoJicQ==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    dependencies:
      ajv: 6.12.6
      debug: 4.3.4
      espree: 9.5.2
      globals: 13.20.0
      ignore: 5.2.4
      import-fresh: 3.3.0
      js-yaml: 4.1.0
      minimatch: 3.1.2
      strip-json-comments: 3.1.1
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@eslint/js@8.38.0:
    resolution: {integrity: sha512-IoD2MfUnOV58ghIHCiil01PcohxjbYR/qCxsoC+xNgUwh1EY8jOOrYmu3d3a71+tJJ23uscEV4X2HJWMsPJu4g==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    dev: true

  /@fortawesome/fontawesome-common-types@6.4.0:
    resolution: {integrity: sha512-HNii132xfomg5QVZw0HwXXpN22s7VBHQBv9CeOu9tfJnhsWQNd2lmTNi8CSrnw5B+5YOmzu1UoPAyxaXsJ6RgQ==}
    engines: {node: '>=6'}
    requiresBuild: true
    dev: false

  /@fortawesome/fontawesome-svg-core@6.4.0:
    resolution: {integrity: sha512-Bertv8xOiVELz5raB2FlXDPKt+m94MQ3JgDfsVbrqNpLU9+UE2E18GKjLKw+d3XbeYPqg1pzyQKGsrzbw+pPaw==}
    engines: {node: '>=6'}
    requiresBuild: true
    dependencies:
      '@fortawesome/fontawesome-common-types': 6.4.0
    dev: false

  /@fortawesome/free-brands-svg-icons@6.4.0:
    resolution: {integrity: sha512-qvxTCo0FQ5k2N+VCXb/PZQ+QMhqRVM4OORiO6MXdG6bKolIojGU/srQ1ptvKk0JTbRgaJOfL2qMqGvBEZG7Z6g==}
    engines: {node: '>=6'}
    requiresBuild: true
    dependencies:
      '@fortawesome/fontawesome-common-types': 6.4.0
    dev: false

  /@fortawesome/free-regular-svg-icons@6.4.0:
    resolution: {integrity: sha512-ZfycI7D0KWPZtf7wtMFnQxs8qjBXArRzczABuMQqecA/nXohquJ5J/RCR77PmY5qGWkxAZDxpnUFVXKwtY/jPw==}
    engines: {node: '>=6'}
    requiresBuild: true
    dependencies:
      '@fortawesome/fontawesome-common-types': 6.4.0
    dev: false

  /@fortawesome/free-solid-svg-icons@6.4.0:
    resolution: {integrity: sha512-kutPeRGWm8V5dltFP1zGjQOEAzaLZj4StdQhWVZnfGFCvAPVvHh8qk5bRrU4KXnRRRNni5tKQI9PBAdI6MP8nQ==}
    engines: {node: '>=6'}
    requiresBuild: true
    dependencies:
      '@fortawesome/fontawesome-common-types': 6.4.0
    dev: false

  /@fortawesome/react-fontawesome@0.2.0(@fortawesome/fontawesome-svg-core@6.4.0)(react@18.2.0):
    resolution: {integrity: sha512-uHg75Rb/XORTtVt7OS9WoK8uM276Ufi7gCzshVWkUJbHhh3svsUUeqXerrM96Wm7fRiDzfKRwSoahhMIkGAYHw==}
    peerDependencies:
      '@fortawesome/fontawesome-svg-core': ~1 || ~6
      react: '>=16.3'
    dependencies:
      '@fortawesome/fontawesome-svg-core': 6.4.0
      prop-types: 15.8.1
      react: 18.2.0
    dev: false

  /@headlessui/react@1.7.15(react-dom@18.2.0)(react@18.2.0):
    resolution: {integrity: sha512-OTO0XtoRQ6JPB1cKNFYBZv2Q0JMqMGNhYP1CjPvcJvjz8YGokz8oAj89HIYZGN0gZzn/4kk9iUpmMF4Q21Gsqw==}
    engines: {node: '>=10'}
    peerDependencies:
      react: ^16 || ^17 || ^18
      react-dom: ^16 || ^17 || ^18
    dependencies:
      client-only: 0.0.1
      react: 18.2.0
      react-dom: 18.2.0(react@18.2.0)
    dev: false

  /@humanwhocodes/config-array@0.11.10:
    resolution: {integrity: sha512-KVVjQmNUepDVGXNuoRRdmmEjruj0KfiGSbS8LVc12LMsWDQzRXJ0qdhN8L8uUigKpfEHRhlaQFY0ib1tnUbNeQ==}
    engines: {node: '>=10.10.0'}
    dependencies:
      '@humanwhocodes/object-schema': 1.2.1
      debug: 4.3.4
      minimatch: 3.1.2
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@humanwhocodes/module-importer@1.0.1:
    resolution: {integrity: sha512-bxveV4V8v5Yb4ncFTT3rPSgZBOpCkjfK0y4oVVVJwIuDVBRMDXrPyXRL988i5ap9m9bnyEEjWfm5WkBmtffLfA==}
    engines: {node: '>=12.22'}
    dev: true

  /@humanwhocodes/object-schema@1.2.1:
    resolution: {integrity: sha512-ZnQMnLV4e7hDlUvw8H+U8ASL02SS2Gn6+9Ac3wGGLIe7+je2AeAOxPY+izIPJDfFDb7eDjev0Us8MO1iFRN8hA==}
    dev: true

  /@jridgewell/gen-mapping@0.3.3:
    resolution: {integrity: sha512-HLhSWOLRi875zjjMG/r+Nv0oCW8umGb0BgEhyX3dDX3egwZtB8PqLnjz3yedt8R5StBrzcg4aBpnh8UA9D1BoQ==}
    engines: {node: '>=6.0.0'}
    dependencies:
      '@jridgewell/set-array': 1.1.2
      '@jridgewell/sourcemap-codec': 1.4.15
      '@jridgewell/trace-mapping': 0.3.18
    dev: true

  /@jridgewell/resolve-uri@3.1.0:
    resolution: {integrity: sha512-F2msla3tad+Mfht5cJq7LSXcdudKTWCVYUgw6pLFOOHSTtZlj6SWNYAp+AhuqLmWdBO2X5hPrLcu8cVP8fy28w==}
    engines: {node: '>=6.0.0'}
    dev: true

  /@jridgewell/set-array@1.1.2:
    resolution: {integrity: sha512-xnkseuNADM0gt2bs+BvhO0p78Mk762YnZdsuzFV018NoG1Sj1SCQvpSqa7XUaTam5vAGasABV9qXASMKnFMwMw==}
    engines: {node: '>=6.0.0'}
    dev: true

  /@jridgewell/sourcemap-codec@1.4.14:
    resolution: {integrity: sha512-XPSJHWmi394fuUuzDnGz1wiKqWfo1yXecHQMRf2l6hztTO+nPru658AyDngaBe7isIxEkRsPR3FZh+s7iVa4Uw==}
    dev: true

  /@jridgewell/sourcemap-codec@1.4.15:
    resolution: {integrity: sha512-eF2rxCRulEKXHTRiDrDy6erMYWqNw4LPdQ8UQA4huuxaQsVeRPFl2oM8oDGxMFhJUWZf9McpLtJasDDZb/Bpeg==}
    dev: true

  /@jridgewell/trace-mapping@0.3.18:
    resolution: {integrity: sha512-w+niJYzMHdd7USdiH2U6869nqhD2nbfZXND5Yp93qIbEmnDNk7PD48o+YchRVpzMU7M6jVCbenTR7PA1FLQ9pA==}
    dependencies:
      '@jridgewell/resolve-uri': 3.1.0
      '@jridgewell/sourcemap-codec': 1.4.14
    dev: true

  /@ledgerhq/connect-kit-loader@1.1.0:
    resolution: {integrity: sha512-HUy12FEczoWY2FPubnsm1uOA8tkVWc0j90i47suThV3C9NL2xx69ZAIEU3Ytzs2bwLek9S1Q2S1VQJvA+3Ygkg==}
    dev: false

  /@lit-labs/ssr-dom-shim@1.1.1:
    resolution: {integrity: sha512-kXOeFbfCm4fFf2A3WwVEeQj55tMZa8c8/f9AKHMobQMkzNUfUj+antR3fRPaZJawsa1aZiP/Da3ndpZrwEe4rQ==}
    dev: false

  /@lit/reactive-element@1.6.2:
    resolution: {integrity: sha512-rDfl+QnCYjuIGf5xI2sVJWdYIi56CTCwWa+nidKYX6oIuBYwUbT/vX4qbUDlHiZKJ/3FRNQ/tWJui44p6/stSA==}
    dependencies:
      '@lit-labs/ssr-dom-shim': 1.1.1
    dev: false

  /@metamask/safe-event-emitter@2.0.0:
    resolution: {integrity: sha512-/kSXhY692qiV1MXu6EeOZvg5nECLclxNXcKCxJ3cXQgYuRymRHpdx/t7JXfsK+JLjwA1e1c1/SBrlQYpusC29Q==}
    dev: false

  /@metamask/utils@3.6.0:
    resolution: {integrity: sha512-9cIRrfkWvHblSiNDVXsjivqa9Ak0RYo/1H6tqTqTbAx+oBK2Sva0lWDHxGchOqA7bySGUJKAWSNJvH6gdHZ0gQ==}
    engines: {node: '>=14.0.0'}
    dependencies:
      '@types/debug': 4.1.8
      debug: 4.3.4
      semver: 7.5.1
      superstruct: 1.0.3
    transitivePeerDependencies:
      - supports-color
    dev: false

  /@motionone/animation@10.15.1:
    resolution: {integrity: sha512-mZcJxLjHor+bhcPuIFErMDNyrdb2vJur8lSfMCsuCB4UyV8ILZLvK+t+pg56erv8ud9xQGK/1OGPt10agPrCyQ==}
    dependencies:
      '@motionone/easing': 10.15.1
      '@motionone/types': 10.15.1
      '@motionone/utils': 10.15.1
      tslib: 2.6.0
    dev: false

  /@motionone/dom@10.16.2:
    resolution: {integrity: sha512-bnuHdNbge1FutZXv+k7xub9oPWcF0hsu8y1HTH/qg6av58YI0VufZ3ngfC7p2xhMJMnoh0LXFma2EGTgPeCkeg==}
    dependencies:
      '@motionone/animation': 10.15.1
      '@motionone/generators': 10.15.1
      '@motionone/types': 10.15.1
      '@motionone/utils': 10.15.1
      hey-listen: 1.0.8
      tslib: 2.6.0
    dev: false

  /@motionone/easing@10.15.1:
    resolution: {integrity: sha512-6hIHBSV+ZVehf9dcKZLT7p5PEKHGhDwky2k8RKkmOvUoYP3S+dXsKupyZpqx5apjd9f+php4vXk4LuS+ADsrWw==}
    dependencies:
      '@motionone/utils': 10.15.1
      tslib: 2.6.0
    dev: false

  /@motionone/generators@10.15.1:
    resolution: {integrity: sha512-67HLsvHJbw6cIbLA/o+gsm7h+6D4Sn7AUrB/GPxvujse1cGZ38F5H7DzoH7PhX+sjvtDnt2IhFYF2Zp1QTMKWQ==}
    dependencies:
      '@motionone/types': 10.15.1
      '@motionone/utils': 10.15.1
      tslib: 2.6.0
    dev: false

  /@motionone/svelte@10.16.2:
    resolution: {integrity: sha512-38xsroKrfK+aHYhuQlE6eFcGy0EwrB43Q7RGjF73j/kRUTcLNu/LAaKiLLsN5lyqVzCgTBVt4TMT/ShWbTbc5Q==}
    dependencies:
      '@motionone/dom': 10.16.2
      tslib: 2.6.0
    dev: false

  /@motionone/types@10.15.1:
    resolution: {integrity: sha512-iIUd/EgUsRZGrvW0jqdst8st7zKTzS9EsKkP+6c6n4MPZoQHwiHuVtTQLD6Kp0bsBLhNzKIBlHXponn/SDT4hA==}
    dev: false

  /@motionone/utils@10.15.1:
    resolution: {integrity: sha512-p0YncgU+iklvYr/Dq4NobTRdAPv9PveRDUXabPEeOjBLSO/1FNB2phNTZxOxpi1/GZwYpAoECEa0Wam+nsmhSw==}
    dependencies:
      '@motionone/types': 10.15.1
      hey-listen: 1.0.8
      tslib: 2.6.0
    dev: false

  /@motionone/vue@10.16.2:
    resolution: {integrity: sha512-7/dEK/nWQXOkJ70bqb2KyNfSWbNvWqKKq1C8juj+0Mg/AorgD8O5wE3naddK0G+aXuNMqRuc4jlsYHHWHtIzVw==}
    dependencies:
      '@motionone/dom': 10.16.2
      tslib: 2.6.0
    dev: false

  /@noble/curves@1.0.0:
    resolution: {integrity: sha512-2upgEu0iLiDVDZkNLeFV2+ht0BAVgQnEmCk6JsOch9Rp8xfkMCbvbAZlA2pBHQc73dbl+vFOXfqkf4uemdn0bw==}
    dependencies:
      '@noble/hashes': 1.3.0
    dev: false

  /@noble/curves@1.1.0:
    resolution: {integrity: sha512-091oBExgENk/kGj3AZmtBDMpxQPDtxQABR2B9lb1JbVTs6ytdzZNwvhxQ4MWasRNEzlbEH8jCWFCwhF/Obj5AA==}
    dependencies:
      '@noble/hashes': 1.3.1
    dev: false

  /@noble/hashes@1.3.0:
    resolution: {integrity: sha512-ilHEACi9DwqJB0pw7kv+Apvh50jiiSyR/cQ3y4W7lOR5mhvn/50FLUfsnfJz0BDZtl/RR16kXvptiv6q1msYZg==}
    dev: false

  /@noble/hashes@1.3.1:
    resolution: {integrity: sha512-EbqwksQwz9xDRGfDST86whPBgM65E0OH/pCgqW0GBVzO22bNE+NuIbeTb714+IfSjU3aRk47EUvXIb5bTsenKA==}
    engines: {node: '>= 16'}
    dev: false

  /@nodelib/fs.scandir@2.1.5:
    resolution: {integrity: sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==}
    engines: {node: '>= 8'}
    dependencies:
      '@nodelib/fs.stat': 2.0.5
      run-parallel: 1.2.0
    dev: true

  /@nodelib/fs.stat@2.0.5:
    resolution: {integrity: sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==}
    engines: {node: '>= 8'}
    dev: true

  /@nodelib/fs.walk@1.2.8:
    resolution: {integrity: sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==}
    engines: {node: '>= 8'}
    dependencies:
      '@nodelib/fs.scandir': 2.1.5
      fastq: 1.15.0
    dev: true

  /@rainbow-me/rainbowkit@1.0.7(@types/react@18.0.37)(react-dom@18.2.0)(react@18.2.0)(viem@1.4.1)(wagmi@1.3.9):
    resolution: {integrity: sha512-cZZgPqpkeQEmKX5As3+WnKFF7PejDFVbc4bF9t6zC52nMFjSQUAnv2AttzyR4sP4pp2BSE1nVpTvygZGJ4f1Xg==}
    engines: {node: '>=12.4'}
    peerDependencies:
      react: '>=17'
      react-dom: '>=17'
      viem: ~0.3.19 || ^1.0.0
      wagmi: ~1.0.1 || ~1.1.0 || ~1.2.0 || ~1.3.0
    dependencies:
      '@vanilla-extract/css': 1.9.1
      '@vanilla-extract/dynamic': 2.0.2
      '@vanilla-extract/sprinkles': 1.5.0(@vanilla-extract/css@1.9.1)
      clsx: 1.1.1
      qrcode: 1.5.0
      react: 18.2.0
      react-dom: 18.2.0(react@18.2.0)
      react-remove-scroll: 2.5.4(@types/react@18.0.37)(react@18.2.0)
      viem: 1.4.1(typescript@5.0.2)
      wagmi: 1.3.9(react-dom@18.2.0)(react@18.2.0)(typescript@5.0.2)(viem@1.4.1)
    transitivePeerDependencies:
      - '@types/react'
    dev: false

  /@safe-global/safe-apps-provider@0.17.1(typescript@5.0.2):
    resolution: {integrity: sha512-lYfRqrbbK1aKU1/UGkYWc/X7PgySYcumXKc5FB2uuwAs2Ghj8uETuW5BrwPqyjBknRxutFbTv+gth/JzjxAhdQ==}
    dependencies:
      '@safe-global/safe-apps-sdk': 8.0.0(typescript@5.0.2)
      events: 3.3.0
    transitivePeerDependencies:
      - bufferutil
      - encoding
      - typescript
      - utf-8-validate
      - zod
    dev: false

  /@safe-global/safe-apps-sdk@8.0.0(typescript@5.0.2):
    resolution: {integrity: sha512-gYw0ki/EAuV1oSyMxpqandHjnthZjYYy+YWpTAzf8BqfXM3ItcZLpjxfg+3+mXW8HIO+3jw6T9iiqEXsqHaMMw==}
    dependencies:
      '@safe-global/safe-gateway-typescript-sdk': 3.7.3
      viem: 1.4.1(typescript@5.0.2)
    transitivePeerDependencies:
      - bufferutil
      - encoding
      - typescript
      - utf-8-validate
      - zod
    dev: false

  /@safe-global/safe-gateway-typescript-sdk@3.7.3:
    resolution: {integrity: sha512-O6JCgXNZWG0Vv8FnOEjKfcbsP0WxGvoPJk5ufqUrsyBlHup16It6oaLnn+25nXFLBZOHI1bz8429JlqAc2t2hg==}
    dependencies:
      cross-fetch: 3.1.8
    transitivePeerDependencies:
      - encoding
    dev: false

  /@scure/base@1.1.1:
    resolution: {integrity: sha512-ZxOhsSyxYwLJj3pLZCefNitxsj093tb2vq90mp2txoYeBqbcjDjqFhyM8eUjq/uFm6zJ+mUuqxlS2FkuSY1MTA==}
    dev: false

  /@scure/bip32@1.3.0:
    resolution: {integrity: sha512-bcKpo1oj54hGholplGLpqPHRbIsnbixFtc06nwuNM5/dwSXOq/AAYoIBRsBmnZJSdfeNW5rnff7NTAz3ZCqR9Q==}
    dependencies:
      '@noble/curves': 1.0.0
      '@noble/hashes': 1.3.0
      '@scure/base': 1.1.1
    dev: false

  /@scure/bip39@1.2.0:
    resolution: {integrity: sha512-SX/uKq52cuxm4YFXWFaVByaSHJh2w3BnokVSeUJVCv6K7WulT9u2BuNRBhuFl8vAuYnzx9bEu9WgpcNYTrYieg==}
    dependencies:
      '@noble/hashes': 1.3.0
      '@scure/base': 1.1.1
    dev: false

  /@solana/buffer-layout@4.0.1:
    resolution: {integrity: sha512-E1ImOIAD1tBZFRdjeM4/pzTiTApC0AOBGwyAMS4fwIodCWArzJ3DWdoh8cKxeFM2fElkxBh2Aqts1BPC373rHA==}
    engines: {node: '>=5.10'}
    dependencies:
      buffer: 6.0.3
    dev: false

  /@solana/web3.js@1.78.0:
    resolution: {integrity: sha512-CSjCjo+RELJ5puoZALfznN5EF0YvL1V8NQrQYovsdjE1lCV6SqbKAIZD0+9LlqCBoa1ibuUaR7G2SooYzvzmug==}
    dependencies:
      '@babel/runtime': 7.22.6
      '@noble/curves': 1.1.0
      '@noble/hashes': 1.3.1
      '@solana/buffer-layout': 4.0.1
      agentkeepalive: 4.3.0
      bigint-buffer: 1.1.5
      bn.js: 5.2.1
      borsh: 0.7.0
      bs58: 4.0.1
      buffer: 6.0.3
      fast-stable-stringify: 1.0.0
      jayson: 4.1.0
      node-fetch: 2.6.12
      rpc-websockets: 7.5.1
      superstruct: 0.14.2
    transitivePeerDependencies:
      - bufferutil
      - encoding
      - supports-color
      - utf-8-validate
    dev: false

  /@stablelib/aead@1.0.1:
    resolution: {integrity: sha512-q39ik6sxGHewqtO0nP4BuSe3db5G1fEJE8ukvngS2gLkBXyy6E7pLubhbYgnkDFv6V8cWaxcE4Xn0t6LWcJkyg==}
    dev: false

  /@stablelib/binary@1.0.1:
    resolution: {integrity: sha512-ClJWvmL6UBM/wjkvv/7m5VP3GMr9t0osr4yVgLZsLCOz4hGN9gIAFEqnJ0TsSMAN+n840nf2cHZnA5/KFqHC7Q==}
    dependencies:
      '@stablelib/int': 1.0.1
    dev: false

  /@stablelib/bytes@1.0.1:
    resolution: {integrity: sha512-Kre4Y4kdwuqL8BR2E9hV/R5sOrUj6NanZaZis0V6lX5yzqC3hBuVSDXUIBqQv/sCpmuWRiHLwqiT1pqqjuBXoQ==}
    dev: false

  /@stablelib/chacha20poly1305@1.0.1:
    resolution: {integrity: sha512-MmViqnqHd1ymwjOQfghRKw2R/jMIGT3wySN7cthjXCBdO+qErNPUBnRzqNpnvIwg7JBCg3LdeCZZO4de/yEhVA==}
    dependencies:
      '@stablelib/aead': 1.0.1
      '@stablelib/binary': 1.0.1
      '@stablelib/chacha': 1.0.1
      '@stablelib/constant-time': 1.0.1
      '@stablelib/poly1305': 1.0.1
      '@stablelib/wipe': 1.0.1
    dev: false

  /@stablelib/chacha@1.0.1:
    resolution: {integrity: sha512-Pmlrswzr0pBzDofdFuVe1q7KdsHKhhU24e8gkEwnTGOmlC7PADzLVxGdn2PoNVBBabdg0l/IfLKg6sHAbTQugg==}
    dependencies:
      '@stablelib/binary': 1.0.1
      '@stablelib/wipe': 1.0.1
    dev: false

  /@stablelib/constant-time@1.0.1:
    resolution: {integrity: sha512-tNOs3uD0vSJcK6z1fvef4Y+buN7DXhzHDPqRLSXUel1UfqMB1PWNsnnAezrKfEwTLpN0cGH2p9NNjs6IqeD0eg==}
    dev: false

  /@stablelib/ed25519@1.0.3:
    resolution: {integrity: sha512-puIMWaX9QlRsbhxfDc5i+mNPMY+0TmQEskunY1rZEBPi1acBCVQAhnsk/1Hk50DGPtVsZtAWQg4NHGlVaO9Hqg==}
    dependencies:
      '@stablelib/random': 1.0.2
      '@stablelib/sha512': 1.0.1
      '@stablelib/wipe': 1.0.1
    dev: false

  /@stablelib/hash@1.0.1:
    resolution: {integrity: sha512-eTPJc/stDkdtOcrNMZ6mcMK1e6yBbqRBaNW55XA1jU8w/7QdnCF0CmMmOD1m7VSkBR44PWrMHU2l6r8YEQHMgg==}
    dev: false

  /@stablelib/hkdf@1.0.1:
    resolution: {integrity: sha512-SBEHYE16ZXlHuaW5RcGk533YlBj4grMeg5TooN80W3NpcHRtLZLLXvKyX0qcRFxf+BGDobJLnwkvgEwHIDBR6g==}
    dependencies:
      '@stablelib/hash': 1.0.1
      '@stablelib/hmac': 1.0.1
      '@stablelib/wipe': 1.0.1
    dev: false

  /@stablelib/hmac@1.0.1:
    resolution: {integrity: sha512-V2APD9NSnhVpV/QMYgCVMIYKiYG6LSqw1S65wxVoirhU/51ACio6D4yDVSwMzuTJXWZoVHbDdINioBwKy5kVmA==}
    dependencies:
      '@stablelib/constant-time': 1.0.1
      '@stablelib/hash': 1.0.1
      '@stablelib/wipe': 1.0.1
    dev: false

  /@stablelib/int@1.0.1:
    resolution: {integrity: sha512-byr69X/sDtDiIjIV6m4roLVWnNNlRGzsvxw+agj8CIEazqWGOQp2dTYgQhtyVXV9wpO6WyXRQUzLV/JRNumT2w==}
    dev: false

  /@stablelib/keyagreement@1.0.1:
    resolution: {integrity: sha512-VKL6xBwgJnI6l1jKrBAfn265cspaWBPAPEc62VBQrWHLqVgNRE09gQ/AnOEyKUWrrqfD+xSQ3u42gJjLDdMDQg==}
    dependencies:
      '@stablelib/bytes': 1.0.1
    dev: false

  /@stablelib/poly1305@1.0.1:
    resolution: {integrity: sha512-1HlG3oTSuQDOhSnLwJRKeTRSAdFNVB/1djy2ZbS35rBSJ/PFqx9cf9qatinWghC2UbfOYD8AcrtbUQl8WoxabA==}
    dependencies:
      '@stablelib/constant-time': 1.0.1
      '@stablelib/wipe': 1.0.1
    dev: false

  /@stablelib/random@1.0.2:
    resolution: {integrity: sha512-rIsE83Xpb7clHPVRlBj8qNe5L8ISQOzjghYQm/dZ7VaM2KHYwMW5adjQjrzTZCchFnNCNhkwtnOBa9HTMJCI8w==}
    dependencies:
      '@stablelib/binary': 1.0.1
      '@stablelib/wipe': 1.0.1
    dev: false

  /@stablelib/sha256@1.0.1:
    resolution: {integrity: sha512-GIIH3e6KH+91FqGV42Kcj71Uefd/QEe7Dy42sBTeqppXV95ggCcxLTk39bEr+lZfJmp+ghsR07J++ORkRELsBQ==}
    dependencies:
      '@stablelib/binary': 1.0.1
      '@stablelib/hash': 1.0.1
      '@stablelib/wipe': 1.0.1
    dev: false

  /@stablelib/sha512@1.0.1:
    resolution: {integrity: sha512-13gl/iawHV9zvDKciLo1fQ8Bgn2Pvf7OV6amaRVKiq3pjQ3UmEpXxWiAfV8tYjUpeZroBxtyrwtdooQT/i3hzw==}
    dependencies:
      '@stablelib/binary': 1.0.1
      '@stablelib/hash': 1.0.1
      '@stablelib/wipe': 1.0.1
    dev: false

  /@stablelib/wipe@1.0.1:
    resolution: {integrity: sha512-WfqfX/eXGiAd3RJe4VU2snh/ZPwtSjLG4ynQ/vYzvghTh7dHFcI1wl+nrkWG6lGhukOxOsUHfv8dUXr58D0ayg==}
    dev: false

  /@stablelib/x25519@1.0.3:
    resolution: {integrity: sha512-KnTbKmUhPhHavzobclVJQG5kuivH+qDLpe84iRqX3CLrKp881cF160JvXJ+hjn1aMyCwYOKeIZefIH/P5cJoRw==}
    dependencies:
      '@stablelib/keyagreement': 1.0.1
      '@stablelib/random': 1.0.2
      '@stablelib/wipe': 1.0.1
    dev: false

  /@tanstack/query-core@4.32.0:
    resolution: {integrity: sha512-ei4IYwL2kmlKSlCw9WgvV7PpXi0MiswVwfQRxawhJA690zWO3dU49igaQ/UMTl+Jy9jj9dK5IKAYvbX7kUvviQ==}
    dev: false

  /@tanstack/query-persist-client-core@4.32.0:
    resolution: {integrity: sha512-TUIArpiZJqLsYEPmg2LsZD+uJknrAHXWSaoCROFniDS0TqExe4KkjQ2gt+XTBwzxlOEN52R+l98k+oS/u94ogg==}
    dependencies:
      '@tanstack/query-core': 4.32.0
    dev: false

  /@tanstack/query-sync-storage-persister@4.32.0:
    resolution: {integrity: sha512-DJuHgyHmmzjamC1hjs5BB1fScqMXuk/rOYrcmSLOd3U/tceAK0PqZOJzzd2Zt0bwtJQ8hatKqks7MqiLAvAPQw==}
    dependencies:
      '@tanstack/query-persist-client-core': 4.32.0
    dev: false

  /@tanstack/react-query-persist-client@4.32.0(@tanstack/react-query@4.32.0):
    resolution: {integrity: sha512-2H1Fuw02uoW2U4kAexV3rmSjyOWunaWAoMgRybULu/TbEGh00c6p4yon/nQM81TAbf4M66Aa7nU0vqipY0VJXQ==}
    peerDependencies:
      '@tanstack/react-query': 4.32.0
    dependencies:
      '@tanstack/query-persist-client-core': 4.32.0
      '@tanstack/react-query': 4.32.0(react-dom@18.2.0)(react@18.2.0)
    dev: false

  /@tanstack/react-query@4.32.0(react-dom@18.2.0)(react@18.2.0):
    resolution: {integrity: sha512-B8WUMcByYAH9500ENejDCATOmEZhqjtS9wsfiQ3BNa+s+yAynY8SESI8WWHhSqUmjd0pmCSFRP6BOUGSda3QXA==}
    peerDependencies:
      react: ^16.8.0 || ^17.0.0 || ^18.0.0
      react-dom: ^16.8.0 || ^17.0.0 || ^18.0.0
      react-native: '*'
    peerDependenciesMeta:
      react-dom:
        optional: true
      react-native:
        optional: true
    dependencies:
      '@tanstack/query-core': 4.32.0
      react: 18.2.0
      react-dom: 18.2.0(react@18.2.0)
      use-sync-external-store: 1.2.0(react@18.2.0)
    dev: false

  /@types/connect@3.4.35:
    resolution: {integrity: sha512-cdeYyv4KWoEgpBISTxWvqYsVy444DOqehiF3fM3ne10AmJ62RSyNkUnxMJXHQWRQQX2eR94m5y1IZyDwBjV9FQ==}
    dependencies:
      '@types/node': 12.20.55
    dev: false

  /@types/debug@4.1.8:
    resolution: {integrity: sha512-/vPO1EPOs306Cvhwv7KfVfYvOJqA/S/AXjaHQiJboCZzcNDb+TIJFN9/2C9DZ//ijSKWioNyUxD792QmDJ+HKQ==}
    dependencies:
      '@types/ms': 0.7.31
    dev: false

  /@types/json-schema@7.0.12:
    resolution: {integrity: sha512-Hr5Jfhc9eYOQNPYO5WLDq/n4jqijdHNlDXjuAQkkt+mWdQR+XJToOHrsD4cPaMXpn6KO7y2+wM8AZEs8VpBLVA==}
    dev: true

  /@types/ms@0.7.31:
    resolution: {integrity: sha512-iiUgKzV9AuaEkZqkOLDIvlQiL6ltuZd9tGcW3gwpnX8JbuiuhFlEGmmFXEXkN50Cvq7Os88IY2v0dkDqXYWVgA==}
    dev: false

  /@types/node@12.20.55:
    resolution: {integrity: sha512-J8xLz7q2OFulZ2cyGTLE1TbbZcjpno7FaN6zdJNrgAdrJ+DZzh/uFR6YrTb4C+nXakvud8Q4+rbhoIWlYQbUFQ==}
    dev: false

  /@types/p5@1.6.2:
    resolution: {integrity: sha512-iy1B7DBMc9e5j0DrWnIjSJh+Ro9UkKxPHspbx/GvIeGFTOIJF0H2lICnIN4go1OZEAQSHBinLd7t+oe8lrrLvA==}
    dev: false

  /@types/prop-types@15.7.5:
    resolution: {integrity: sha512-JCB8C6SnDoQf0cNycqd/35A7MjcnK+ZTqE7judS6o7utxUCg6imJg3QK2qzHKszlTjcj2cn+NwMB2i96ubpj7w==}

  /@types/react-dom@18.0.11:
    resolution: {integrity: sha512-O38bPbI2CWtgw/OoQoY+BRelw7uysmXbWvw3nLWO21H1HSh+GOlqPuXshJfjmpNlKiiSDG9cc1JZAaMmVdcTlw==}
    dependencies:
      '@types/react': 18.0.37
    dev: true

  /@types/react@18.0.37:
    resolution: {integrity: sha512-4yaZZtkRN3ZIQD3KSEwkfcik8s0SWV+82dlJot1AbGYHCzJkWP3ENBY6wYeDRmKZ6HkrgoGAmR2HqdwYGp6OEw==}
    dependencies:
      '@types/prop-types': 15.7.5
      '@types/scheduler': 0.16.3
      csstype: 3.1.2

  /@types/scheduler@0.16.3:
    resolution: {integrity: sha512-5cJ8CB4yAx7BH1oMvdU0Jh9lrEXyPkar6F9G/ERswkCuvP4KQZfZkSjcMbAICCpQTN4OuZn8tz0HiKv9TGZgrQ==}

  /@types/semver@7.5.0:
    resolution: {integrity: sha512-G8hZ6XJiHnuhQKR7ZmysCeJWE08o8T0AXtk5darsCaTVsYZhhgUrq53jizaR2FvsoeCwJhlmwTjkXBY5Pn/ZHw==}
    dev: true

  /@types/trusted-types@2.0.3:
    resolution: {integrity: sha512-NfQ4gyz38SL8sDNrSixxU2Os1a5xcdFxipAFxYEuLUlvU2uDwS4NUpsImcf1//SlWItCVMMLiylsxbmNMToV/g==}
    dev: false

  /@types/ws@7.4.7:
    resolution: {integrity: sha512-JQbbmxZTZehdc2iszGKs5oC3NFnjeay7mtAWrdt7qNtAVK0g19muApzAy4bm9byz79xa2ZnO/BOBC2R8RC5Lww==}
    dependencies:
      '@types/node': 12.20.55
    dev: false

  /@typescript-eslint/eslint-plugin@5.59.0(@typescript-eslint/parser@5.59.0)(eslint@8.38.0)(typescript@5.0.2):
    resolution: {integrity: sha512-p0QgrEyrxAWBecR56gyn3wkG15TJdI//eetInP3zYRewDh0XS+DhB3VUAd3QqvziFsfaQIoIuZMxZRB7vXYaYw==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    peerDependencies:
      '@typescript-eslint/parser': ^5.0.0
      eslint: ^6.0.0 || ^7.0.0 || ^8.0.0
      typescript: '*'
    peerDependenciesMeta:
      typescript:
        optional: true
    dependencies:
      '@eslint-community/regexpp': 4.5.1
      '@typescript-eslint/parser': 5.59.0(eslint@8.38.0)(typescript@5.0.2)
      '@typescript-eslint/scope-manager': 5.59.0
      '@typescript-eslint/type-utils': 5.59.0(eslint@8.38.0)(typescript@5.0.2)
      '@typescript-eslint/utils': 5.59.0(eslint@8.38.0)(typescript@5.0.2)
      debug: 4.3.4
      eslint: 8.38.0
      grapheme-splitter: 1.0.4
      ignore: 5.2.4
      natural-compare-lite: 1.4.0
      semver: 7.5.1
      tsutils: 3.21.0(typescript@5.0.2)
      typescript: 5.0.2
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@typescript-eslint/parser@5.59.0(eslint@8.38.0)(typescript@5.0.2):
    resolution: {integrity: sha512-qK9TZ70eJtjojSUMrrEwA9ZDQ4N0e/AuoOIgXuNBorXYcBDk397D2r5MIe1B3cok/oCtdNC5j+lUUpVB+Dpb+w==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    peerDependencies:
      eslint: ^6.0.0 || ^7.0.0 || ^8.0.0
      typescript: '*'
    peerDependenciesMeta:
      typescript:
        optional: true
    dependencies:
      '@typescript-eslint/scope-manager': 5.59.0
      '@typescript-eslint/types': 5.59.0
      '@typescript-eslint/typescript-estree': 5.59.0(typescript@5.0.2)
      debug: 4.3.4
      eslint: 8.38.0
      typescript: 5.0.2
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@typescript-eslint/scope-manager@5.59.0:
    resolution: {integrity: sha512-tsoldKaMh7izN6BvkK6zRMINj4Z2d6gGhO2UsI8zGZY3XhLq1DndP3Ycjhi1JwdwPRwtLMW4EFPgpuKhbCGOvQ==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    dependencies:
      '@typescript-eslint/types': 5.59.0
      '@typescript-eslint/visitor-keys': 5.59.0
    dev: true

  /@typescript-eslint/type-utils@5.59.0(eslint@8.38.0)(typescript@5.0.2):
    resolution: {integrity: sha512-d/B6VSWnZwu70kcKQSCqjcXpVH+7ABKH8P1KNn4K7j5PXXuycZTPXF44Nui0TEm6rbWGi8kc78xRgOC4n7xFgA==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    peerDependencies:
      eslint: '*'
      typescript: '*'
    peerDependenciesMeta:
      typescript:
        optional: true
    dependencies:
      '@typescript-eslint/typescript-estree': 5.59.0(typescript@5.0.2)
      '@typescript-eslint/utils': 5.59.0(eslint@8.38.0)(typescript@5.0.2)
      debug: 4.3.4
      eslint: 8.38.0
      tsutils: 3.21.0(typescript@5.0.2)
      typescript: 5.0.2
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@typescript-eslint/types@5.59.0:
    resolution: {integrity: sha512-yR2h1NotF23xFFYKHZs17QJnB51J/s+ud4PYU4MqdZbzeNxpgUr05+dNeCN/bb6raslHvGdd6BFCkVhpPk/ZeA==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    dev: true

  /@typescript-eslint/typescript-estree@5.59.0(typescript@5.0.2):
    resolution: {integrity: sha512-sUNnktjmI8DyGzPdZ8dRwW741zopGxltGs/SAPgGL/AAgDpiLsCFLcMNSpbfXfmnNeHmK9h3wGmCkGRGAoUZAg==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    peerDependencies:
      typescript: '*'
    peerDependenciesMeta:
      typescript:
        optional: true
    dependencies:
      '@typescript-eslint/types': 5.59.0
      '@typescript-eslint/visitor-keys': 5.59.0
      debug: 4.3.4
      globby: 11.1.0
      is-glob: 4.0.3
      semver: 7.5.1
      tsutils: 3.21.0(typescript@5.0.2)
      typescript: 5.0.2
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@typescript-eslint/utils@5.59.0(eslint@8.38.0)(typescript@5.0.2):
    resolution: {integrity: sha512-GGLFd+86drlHSvPgN/el6dRQNYYGOvRSDVydsUaQluwIW3HvbXuxyuD5JETvBt/9qGYe+lOrDk6gRrWOHb/FvA==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    peerDependencies:
      eslint: ^6.0.0 || ^7.0.0 || ^8.0.0
    dependencies:
      '@eslint-community/eslint-utils': 4.4.0(eslint@8.38.0)
      '@types/json-schema': 7.0.12
      '@types/semver': 7.5.0
      '@typescript-eslint/scope-manager': 5.59.0
      '@typescript-eslint/types': 5.59.0
      '@typescript-eslint/typescript-estree': 5.59.0(typescript@5.0.2)
      eslint: 8.38.0
      eslint-scope: 5.1.1
      semver: 7.5.1
    transitivePeerDependencies:
      - supports-color
      - typescript
    dev: true

  /@typescript-eslint/visitor-keys@5.59.0:
    resolution: {integrity: sha512-qZ3iXxQhanchCeaExlKPV3gDQFxMUmU35xfd5eCXB6+kUw1TUAbIy2n7QIrwz9s98DQLzNWyHp61fY0da4ZcbA==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    dependencies:
      '@typescript-eslint/types': 5.59.0
      eslint-visitor-keys: 3.4.1
    dev: true

  /@vanilla-extract/css@1.9.1:
    resolution: {integrity: sha512-pu2SFiff5jRhPwvGoj8cM5l/qIyLvigOmy22ss5DGjwV5pJYezRjDLxWumi2luIwioMWvh9EozCjyfH8nq+7fQ==}
    dependencies:
      '@emotion/hash': 0.8.0
      '@vanilla-extract/private': 1.0.3
      ahocorasick: 1.0.2
      chalk: 4.1.2
      css-what: 5.1.0
      cssesc: 3.0.0
      csstype: 3.1.2
      deep-object-diff: 1.1.9
      deepmerge: 4.3.1
      media-query-parser: 2.0.2
      outdent: 0.8.0
    dev: false

  /@vanilla-extract/dynamic@2.0.2:
    resolution: {integrity: sha512-U4nKaEQ8Kuz+exXEr51DUpyaOuzo24/S/k1YbDPQR06cYcNjQqvwFRnwWtZ+9ImocqM1wTKtzrdUgSTtLGIwAg==}
    dependencies:
      '@vanilla-extract/private': 1.0.3
    dev: false

  /@vanilla-extract/private@1.0.3:
    resolution: {integrity: sha512-17kVyLq3ePTKOkveHxXuIJZtGYs+cSoev7BlP+Lf4916qfDhk/HBjvlYDe8egrea7LNPHKwSZJK/bzZC+Q6AwQ==}
    dev: false

  /@vanilla-extract/sprinkles@1.5.0(@vanilla-extract/css@1.9.1):
    resolution: {integrity: sha512-W58f2Rzz5lLmk0jbhgStVlZl5wEiPB1Ur3fRvUaBM+MrifZ3qskmFq/CiH//fEYeG5Dh9vF1qRviMMH46cX9Nw==}
    peerDependencies:
      '@vanilla-extract/css': ^1.0.0
    dependencies:
      '@vanilla-extract/css': 1.9.1
    dev: false

  /@vitejs/plugin-react@4.0.0(vite@4.3.9):
    resolution: {integrity: sha512-HX0XzMjL3hhOYm+0s95pb0Z7F8O81G7joUHgfDd/9J/ZZf5k4xX6QAMFkKsHFxaHlf6X7GD7+XuaZ66ULiJuhQ==}
    engines: {node: ^14.18.0 || >=16.0.0}
    peerDependencies:
      vite: ^4.2.0
    dependencies:
      '@babel/core': 7.22.1
      '@babel/plugin-transform-react-jsx-self': 7.21.0(@babel/core@7.22.1)
      '@babel/plugin-transform-react-jsx-source': 7.19.6(@babel/core@7.22.1)
      react-refresh: 0.14.0
      vite: 4.3.9(sass@1.63.2)
    transitivePeerDependencies:
      - supports-color
    dev: true

  /@wagmi/chains@1.6.0(typescript@5.0.2):
    resolution: {integrity: sha512-5FRlVxse5P4ZaHG3GTvxwVANSmYJas1eQrTBHhjxVtqXoorm0aLmCHbhmN8Xo1yu09PaWKlleEvfE98yH4AgIw==}
    peerDependencies:
      typescript: '>=5.0.4'
    peerDependenciesMeta:
      typescript:
        optional: true
    dependencies:
      typescript: 5.0.2
    dev: false

  /@wagmi/connectors@2.6.6(@wagmi/chains@1.6.0)(react@18.2.0)(typescript@5.0.2)(viem@1.4.1):
    resolution: {integrity: sha512-/o1c/TCivQs8DOAUOcQvY2UIt3p2mWOAHi39D0LC74+ncpXzLC5/gyaWU38qnTxPM8s/PmTmaWDgz+VhICXrag==}
    peerDependencies:
      '@wagmi/chains': '>=1.3.0'
      typescript: '>=5.0.4'
      viem: '>=0.3.35'
    peerDependenciesMeta:
      '@wagmi/chains':
        optional: true
      typescript:
        optional: true
    dependencies:
      '@coinbase/wallet-sdk': 3.7.1
      '@ledgerhq/connect-kit-loader': 1.1.0
      '@safe-global/safe-apps-provider': 0.17.1(typescript@5.0.2)
      '@safe-global/safe-apps-sdk': 8.0.0(typescript@5.0.2)
      '@wagmi/chains': 1.6.0(typescript@5.0.2)
      '@walletconnect/ethereum-provider': 2.9.0(@walletconnect/modal@2.5.9)
      '@walletconnect/legacy-provider': 2.0.0
      '@walletconnect/modal': 2.5.9(react@18.2.0)
      '@walletconnect/utils': 2.9.0
      abitype: 0.8.7(typescript@5.0.2)
      eventemitter3: 4.0.7
      typescript: 5.0.2
      viem: 1.4.1(typescript@5.0.2)
    transitivePeerDependencies:
      - '@react-native-async-storage/async-storage'
      - bufferutil
      - encoding
      - lokijs
      - react
      - supports-color
      - utf-8-validate
      - zod
    dev: false

  /@wagmi/core@1.3.8(react@18.2.0)(typescript@5.0.2)(viem@1.4.1):
    resolution: {integrity: sha512-OYSxikoMizqVnpSkFTwGE7PwFaz2k0PXteSiI0W2Mtk4j4sZzRFdP+9AWeDB6AYm0yU3WvgN1IATx0EEBKUe3w==}
    peerDependencies:
      typescript: '>=5.0.4'
      viem: '>=0.3.35'
    peerDependenciesMeta:
      typescript:
        optional: true
    dependencies:
      '@wagmi/chains': 1.6.0(typescript@5.0.2)
      '@wagmi/connectors': 2.6.6(@wagmi/chains@1.6.0)(react@18.2.0)(typescript@5.0.2)(viem@1.4.1)
      abitype: 0.8.7(typescript@5.0.2)
      eventemitter3: 4.0.7
      typescript: 5.0.2
      viem: 1.4.1(typescript@5.0.2)
      zustand: 4.3.9(react@18.2.0)
    transitivePeerDependencies:
      - '@react-native-async-storage/async-storage'
      - bufferutil
      - encoding
      - immer
      - lokijs
      - react
      - supports-color
      - utf-8-validate
      - zod
    dev: false

  /@walletconnect/core@2.9.0:
    resolution: {integrity: sha512-MZYJghS9YCvGe32UOgDj0mCasaOoGHQaYXWeQblXE/xb8HuaM6kAWhjIQN9P+MNp5QP134BHP5olQostcCotXQ==}
    dependencies:
      '@walletconnect/heartbeat': 1.2.1
      '@walletconnect/jsonrpc-provider': 1.0.13
      '@walletconnect/jsonrpc-types': 1.0.3
      '@walletconnect/jsonrpc-utils': 1.0.8
      '@walletconnect/jsonrpc-ws-connection': 1.0.12
      '@walletconnect/keyvaluestorage': 1.0.2
      '@walletconnect/logger': 2.0.1
      '@walletconnect/relay-api': 1.0.9
      '@walletconnect/relay-auth': 1.0.4
      '@walletconnect/safe-json': 1.0.2
      '@walletconnect/time': 1.0.2
      '@walletconnect/types': 2.9.0
      '@walletconnect/utils': 2.9.0
      events: 3.3.0
      lodash.isequal: 4.5.0
      uint8arrays: 3.1.1
    transitivePeerDependencies:
      - '@react-native-async-storage/async-storage'
      - bufferutil
      - lokijs
      - utf-8-validate
    dev: false

  /@walletconnect/crypto@1.0.3:
    resolution: {integrity: sha512-+2jdORD7XQs76I2Odgr3wwrtyuLUXD/kprNVsjWRhhhdO9Mt6WqVzOPu0/t7OHSmgal8k7SoBQzUc5hu/8zL/g==}
    dependencies:
      '@walletconnect/encoding': 1.0.2
      '@walletconnect/environment': 1.0.1
      '@walletconnect/randombytes': 1.0.3
      aes-js: 3.1.2
      hash.js: 1.1.7
      tslib: 1.14.1
    dev: false

  /@walletconnect/encoding@1.0.2:
    resolution: {integrity: sha512-CrwSBrjqJ7rpGQcTL3kU+Ief+Bcuu9PH6JLOb+wM6NITX1GTxR/MfNwnQfhLKK6xpRAyj2/nM04OOH6wS8Imag==}
    dependencies:
      is-typedarray: 1.0.0
      tslib: 1.14.1
      typedarray-to-buffer: 3.1.5
    dev: false

  /@walletconnect/environment@1.0.1:
    resolution: {integrity: sha512-T426LLZtHj8e8rYnKfzsw1aG6+M0BT1ZxayMdv/p8yM0MU+eJDISqNY3/bccxRr4LrF9csq02Rhqt08Ibl0VRg==}
    dependencies:
      tslib: 1.14.1
    dev: false

  /@walletconnect/ethereum-provider@2.9.0(@walletconnect/modal@2.5.9):
    resolution: {integrity: sha512-rSXkC0SXMigJRdIi/M2RMuEuATY1AwtlTWQBnqyxoht7xbO2bQNPCXn0XL4s/GRNrSUtoKSY4aPMHXV4W4yLBA==}
    peerDependencies:
      '@walletconnect/modal': '>=2'
    peerDependenciesMeta:
      '@walletconnect/modal':
        optional: true
    dependencies:
      '@walletconnect/jsonrpc-http-connection': 1.0.7
      '@walletconnect/jsonrpc-provider': 1.0.13
      '@walletconnect/jsonrpc-types': 1.0.3
      '@walletconnect/jsonrpc-utils': 1.0.8
      '@walletconnect/modal': 2.5.9(react@18.2.0)
      '@walletconnect/sign-client': 2.9.0
      '@walletconnect/types': 2.9.0
      '@walletconnect/universal-provider': 2.9.0
      '@walletconnect/utils': 2.9.0
      events: 3.3.0
    transitivePeerDependencies:
      - '@react-native-async-storage/async-storage'
      - bufferutil
      - encoding
      - lokijs
      - utf-8-validate
    dev: false

  /@walletconnect/events@1.0.1:
    resolution: {integrity: sha512-NPTqaoi0oPBVNuLv7qPaJazmGHs5JGyO8eEAk5VGKmJzDR7AHzD4k6ilox5kxk1iwiOnFopBOOMLs86Oa76HpQ==}
    dependencies:
      keyvaluestorage-interface: 1.0.0
      tslib: 1.14.1
    dev: false

  /@walletconnect/heartbeat@1.2.1:
    resolution: {integrity: sha512-yVzws616xsDLJxuG/28FqtZ5rzrTA4gUjdEMTbWB5Y8V1XHRmqq4efAxCw5ie7WjbXFSUyBHaWlMR+2/CpQC5Q==}
    dependencies:
      '@walletconnect/events': 1.0.1
      '@walletconnect/time': 1.0.2
      tslib: 1.14.1
    dev: false

  /@walletconnect/jsonrpc-http-connection@1.0.7:
    resolution: {integrity: sha512-qlfh8fCfu8LOM9JRR9KE0s0wxP6ZG9/Jom8M0qsoIQeKF3Ni0FyV4V1qy/cc7nfI46SLQLSl4tgWSfLiE1swyQ==}
    dependencies:
      '@walletconnect/jsonrpc-utils': 1.0.8
      '@walletconnect/safe-json': 1.0.2
      cross-fetch: 3.1.8
      tslib: 1.14.1
    transitivePeerDependencies:
      - encoding
    dev: false

  /@walletconnect/jsonrpc-provider@1.0.13:
    resolution: {integrity: sha512-K73EpThqHnSR26gOyNEL+acEex3P7VWZe6KE12ZwKzAt2H4e5gldZHbjsu2QR9cLeJ8AXuO7kEMOIcRv1QEc7g==}
    dependencies:
      '@walletconnect/jsonrpc-utils': 1.0.8
      '@walletconnect/safe-json': 1.0.2
      tslib: 1.14.1
    dev: false

  /@walletconnect/jsonrpc-types@1.0.3:
    resolution: {integrity: sha512-iIQ8hboBl3o5ufmJ8cuduGad0CQm3ZlsHtujv9Eu16xq89q+BG7Nh5VLxxUgmtpnrePgFkTwXirCTkwJH1v+Yw==}
    dependencies:
      keyvaluestorage-interface: 1.0.0
      tslib: 1.14.1
    dev: false

  /@walletconnect/jsonrpc-utils@1.0.8:
    resolution: {integrity: sha512-vdeb03bD8VzJUL6ZtzRYsFMq1eZQcM3EAzT0a3st59dyLfJ0wq+tKMpmGH7HlB7waD858UWgfIcudbPFsbzVdw==}
    dependencies:
      '@walletconnect/environment': 1.0.1
      '@walletconnect/jsonrpc-types': 1.0.3
      tslib: 1.14.1
    dev: false

  /@walletconnect/jsonrpc-ws-connection@1.0.12:
    resolution: {integrity: sha512-HAcadga3Qjt1Cqy+qXEW6zjaCs8uJGdGQrqltzl3OjiK4epGZRdvSzTe63P+t/3z+D2wG+ffEPn0GVcDozmN1w==}
    dependencies:
      '@walletconnect/jsonrpc-utils': 1.0.8
      '@walletconnect/safe-json': 1.0.2
      events: 3.3.0
      tslib: 1.14.1
      ws: 7.5.9
    transitivePeerDependencies:
      - bufferutil
      - utf-8-validate
    dev: false

  /@walletconnect/keyvaluestorage@1.0.2:
    resolution: {integrity: sha512-U/nNG+VLWoPFdwwKx0oliT4ziKQCEoQ27L5Hhw8YOFGA2Po9A9pULUYNWhDgHkrb0gYDNt//X7wABcEWWBd3FQ==}
    peerDependencies:
      '@react-native-async-storage/async-storage': 1.x
      lokijs: 1.x
    peerDependenciesMeta:
      '@react-native-async-storage/async-storage':
        optional: true
      lokijs:
        optional: true
    dependencies:
      safe-json-utils: 1.1.1
      tslib: 1.14.1
    dev: false

  /@walletconnect/legacy-client@2.0.0:
    resolution: {integrity: sha512-v5L7rYk9loVnfvUf0mF+76bUPFaU5/Vh7mzL6/950CD/yoGdzYZ3Kj+L7mkC6HPMEGeQsBP1+sqBuiVGZ/aODA==}
    dependencies:
      '@walletconnect/crypto': 1.0.3
      '@walletconnect/encoding': 1.0.2
      '@walletconnect/jsonrpc-utils': 1.0.8
      '@walletconnect/legacy-types': 2.0.0
      '@walletconnect/legacy-utils': 2.0.0
      '@walletconnect/safe-json': 1.0.2
      '@walletconnect/window-getters': 1.0.1
      '@walletconnect/window-metadata': 1.0.1
      detect-browser: 5.3.0
      query-string: 6.14.1
    dev: false

  /@walletconnect/legacy-modal@2.0.0:
    resolution: {integrity: sha512-jckNd8lMhm4X7dX9TDdxM3bXKJnaqkRs6K2Mo5j6GmbIF9Eyx40jZ5+q457RVxvM6ciZEDT5s1wBHWdWoOo+9Q==}
    dependencies:
      '@walletconnect/legacy-types': 2.0.0
      '@walletconnect/legacy-utils': 2.0.0
      copy-to-clipboard: 3.3.3
      preact: 10.16.0
      qrcode: 1.5.3
    dev: false

  /@walletconnect/legacy-provider@2.0.0:
    resolution: {integrity: sha512-A8xPebMI1A+50HbWwTpFCbwP7G+1NGKdTKyg8BUUg3h3Y9JucpC1W6w/x0v1Xw7qFEqQnz74LoIN/A3ytH9xrQ==}
    dependencies:
      '@walletconnect/jsonrpc-http-connection': 1.0.7
      '@walletconnect/jsonrpc-provider': 1.0.13
      '@walletconnect/legacy-client': 2.0.0
      '@walletconnect/legacy-modal': 2.0.0
      '@walletconnect/legacy-types': 2.0.0
      '@walletconnect/legacy-utils': 2.0.0
    transitivePeerDependencies:
      - encoding
    dev: false

  /@walletconnect/legacy-types@2.0.0:
    resolution: {integrity: sha512-sOVrA7HUdbI1OwKyPOQU0/DdvTSVFlsXWpAk2K2WvP2erTkBWPMTJq6cv2BmKdoJ3p6gLApT7sd+jHi3OF71uw==}
    dependencies:
      '@walletconnect/jsonrpc-types': 1.0.3
    dev: false

  /@walletconnect/legacy-utils@2.0.0:
    resolution: {integrity: sha512-CPWxSVVXw0kgNCxvU126g4GiV3mzXmC8IPJ15twE46aJ1FX+RHEIfAzFMFz2F2+fEhBxL63A7dwNQKDXorRPcQ==}
    dependencies:
      '@walletconnect/encoding': 1.0.2
      '@walletconnect/jsonrpc-utils': 1.0.8
      '@walletconnect/legacy-types': 2.0.0
      '@walletconnect/safe-json': 1.0.2
      '@walletconnect/window-getters': 1.0.1
      '@walletconnect/window-metadata': 1.0.1
      detect-browser: 5.3.0
      query-string: 6.14.1
    dev: false

  /@walletconnect/logger@2.0.1:
    resolution: {integrity: sha512-SsTKdsgWm+oDTBeNE/zHxxr5eJfZmE9/5yp/Ku+zJtcTAjELb3DXueWkDXmE9h8uHIbJzIb5wj5lPdzyrjT6hQ==}
    dependencies:
      pino: 7.11.0
      tslib: 1.14.1
    dev: false

  /@walletconnect/modal-core@2.5.9(react@18.2.0):
    resolution: {integrity: sha512-isIebwF9hOknGouhS/Ob4YJ9Sa/tqNYG2v6Ua9EkCqIoLimepkG5eC53tslUWW29SLSfQ9qqBNG2+iE7yQXqgw==}
    dependencies:
      buffer: 6.0.3
      valtio: 1.10.6(react@18.2.0)
    transitivePeerDependencies:
      - react
    dev: false

  /@walletconnect/modal-ui@2.5.9(react@18.2.0):
    resolution: {integrity: sha512-nfBaAT9Ls7RZTBBgAq+Nt/3AoUcinIJ9bcq5UHXTV3lOPu/qCKmUC/0HY3GvUK8ykabUAsjr0OAGmcqkB91qug==}
    dependencies:
      '@walletconnect/modal-core': 2.5.9(react@18.2.0)
      lit: 2.7.5
      motion: 10.16.2
      qrcode: 1.5.3
    transitivePeerDependencies:
      - react
    dev: false

  /@walletconnect/modal@2.5.9(react@18.2.0):
    resolution: {integrity: sha512-Zs2RvPwbBNRdBhb50FuJCxi3FJltt1KSpI7odjU/x9GTpTOcSOkmR66PBCy2JvNA0+ztnS1Xs0LVEr3lu7/Jzw==}
    dependencies:
      '@walletconnect/modal-core': 2.5.9(react@18.2.0)
      '@walletconnect/modal-ui': 2.5.9(react@18.2.0)
    transitivePeerDependencies:
      - react
    dev: false

  /@walletconnect/randombytes@1.0.3:
    resolution: {integrity: sha512-35lpzxcHFbTN3ABefC9W+uBpNZl1GC4Wpx0ed30gibfO/y9oLdy1NznbV96HARQKSBV9J9M/rrtIvf6a23jfYw==}
    dependencies:
      '@walletconnect/encoding': 1.0.2
      '@walletconnect/environment': 1.0.1
      randombytes: 2.1.0
      tslib: 1.14.1
    dev: false

  /@walletconnect/relay-api@1.0.9:
    resolution: {integrity: sha512-Q3+rylJOqRkO1D9Su0DPE3mmznbAalYapJ9qmzDgK28mYF9alcP3UwG/og5V7l7CFOqzCLi7B8BvcBUrpDj0Rg==}
    dependencies:
      '@walletconnect/jsonrpc-types': 1.0.3
      tslib: 1.14.1
    dev: false

  /@walletconnect/relay-auth@1.0.4:
    resolution: {integrity: sha512-kKJcS6+WxYq5kshpPaxGHdwf5y98ZwbfuS4EE/NkQzqrDFm5Cj+dP8LofzWvjrrLkZq7Afy7WrQMXdLy8Sx7HQ==}
    dependencies:
      '@stablelib/ed25519': 1.0.3
      '@stablelib/random': 1.0.2
      '@walletconnect/safe-json': 1.0.2
      '@walletconnect/time': 1.0.2
      tslib: 1.14.1
      uint8arrays: 3.1.1
    dev: false

  /@walletconnect/safe-json@1.0.2:
    resolution: {integrity: sha512-Ogb7I27kZ3LPC3ibn8ldyUr5544t3/STow9+lzz7Sfo808YD7SBWk7SAsdBFlYgP2zDRy2hS3sKRcuSRM0OTmA==}
    dependencies:
      tslib: 1.14.1
    dev: false

  /@walletconnect/sign-client@2.9.0:
    resolution: {integrity: sha512-mEKc4LlLMebCe45qzqh+MX4ilQK4kOEBzLY6YJpG8EhyT45eX4JMNA7qQoYa9MRMaaVb/7USJcc4e3ZrjZvQmA==}
    dependencies:
      '@walletconnect/core': 2.9.0
      '@walletconnect/events': 1.0.1
      '@walletconnect/heartbeat': 1.2.1
      '@walletconnect/jsonrpc-utils': 1.0.8
      '@walletconnect/logger': 2.0.1
      '@walletconnect/time': 1.0.2
      '@walletconnect/types': 2.9.0
      '@walletconnect/utils': 2.9.0
      events: 3.3.0
    transitivePeerDependencies:
      - '@react-native-async-storage/async-storage'
      - bufferutil
      - lokijs
      - utf-8-validate
    dev: false

  /@walletconnect/time@1.0.2:
    resolution: {integrity: sha512-uzdd9woDcJ1AaBZRhqy5rNC9laqWGErfc4dxA9a87mPdKOgWMD85mcFo9dIYIts/Jwocfwn07EC6EzclKubk/g==}
    dependencies:
      tslib: 1.14.1
    dev: false

  /@walletconnect/types@2.9.0:
    resolution: {integrity: sha512-ORopsMfSRvUYqtjKKd6scfg8o4/aGebipLxx92AuuUgMTERSU6cGmIrK6rdLu7W6FBJkmngPLEGc9mRqAb9Lug==}
    dependencies:
      '@walletconnect/events': 1.0.1
      '@walletconnect/heartbeat': 1.2.1
      '@walletconnect/jsonrpc-types': 1.0.3
      '@walletconnect/keyvaluestorage': 1.0.2
      '@walletconnect/logger': 2.0.1
      events: 3.3.0
    transitivePeerDependencies:
      - '@react-native-async-storage/async-storage'
      - lokijs
    dev: false

  /@walletconnect/universal-provider@2.9.0:
    resolution: {integrity: sha512-k3nkSBkF69sJJVoe17IVoPtnhp/sgaa2t+x7BvA/BKeMxE0DGdtRJdEXotTc8DBmI7o2tkq6l8+HyFBGjQ/CjQ==}
    dependencies:
      '@walletconnect/jsonrpc-http-connection': 1.0.7
      '@walletconnect/jsonrpc-provider': 1.0.13
      '@walletconnect/jsonrpc-types': 1.0.3
      '@walletconnect/jsonrpc-utils': 1.0.8
      '@walletconnect/logger': 2.0.1
      '@walletconnect/sign-client': 2.9.0
      '@walletconnect/types': 2.9.0
      '@walletconnect/utils': 2.9.0
      events: 3.3.0
    transitivePeerDependencies:
      - '@react-native-async-storage/async-storage'
      - bufferutil
      - encoding
      - lokijs
      - utf-8-validate
    dev: false

  /@walletconnect/utils@2.9.0:
    resolution: {integrity: sha512-7Tu3m6dZL84KofrNBcblsgpSqU2vdo9ImLD7zWimLXERVGNQ8smXG+gmhQYblebIBhsPzjy9N38YMC3nPlfQNw==}
    dependencies:
      '@stablelib/chacha20poly1305': 1.0.1
      '@stablelib/hkdf': 1.0.1
      '@stablelib/random': 1.0.2
      '@stablelib/sha256': 1.0.1
      '@stablelib/x25519': 1.0.3
      '@walletconnect/relay-api': 1.0.9
      '@walletconnect/safe-json': 1.0.2
      '@walletconnect/time': 1.0.2
      '@walletconnect/types': 2.9.0
      '@walletconnect/window-getters': 1.0.1
      '@walletconnect/window-metadata': 1.0.1
      detect-browser: 5.3.0
      query-string: 7.1.3
      uint8arrays: 3.1.1
    transitivePeerDependencies:
      - '@react-native-async-storage/async-storage'
      - lokijs
    dev: false

  /@walletconnect/window-getters@1.0.1:
    resolution: {integrity: sha512-vHp+HqzGxORPAN8gY03qnbTMnhqIwjeRJNOMOAzePRg4xVEEE2WvYsI9G2NMjOknA8hnuYbU3/hwLcKbjhc8+Q==}
    dependencies:
      tslib: 1.14.1
    dev: false

  /@walletconnect/window-metadata@1.0.1:
    resolution: {integrity: sha512-9koTqyGrM2cqFRW517BPY/iEtUDx2r1+Pwwu5m7sJ7ka79wi3EyqhqcICk/yDmv6jAS1rjKgTKXlEhanYjijcA==}
    dependencies:
      '@walletconnect/window-getters': 1.0.1
      tslib: 1.14.1
    dev: false

  /JSONStream@1.3.5:
    resolution: {integrity: sha512-E+iruNOY8VV9s4JEbe1aNEm6MiszPRr/UfcHMz0TQh1BXSxHK+ASV1R6W4HpjBhSeS+54PIsAMCBmwD06LLsqQ==}
    hasBin: true
    dependencies:
      jsonparse: 1.3.1
      through: 2.3.8
    dev: false

  /abitype@0.8.7(typescript@5.0.2):
    resolution: {integrity: sha512-wQ7hV8Yg/yKmGyFpqrNZufCxbszDe5es4AZGYPBitocfSqXtjrTG9JMWFcc4N30ukl2ve48aBTwt7NJxVQdU3w==}
    peerDependencies:
      typescript: '>=5.0.4'
      zod: ^3 >=3.19.1
    peerDependenciesMeta:
      zod:
        optional: true
    dependencies:
      typescript: 5.0.2
    dev: false

  /abitype@0.9.3(typescript@5.0.2):
    resolution: {integrity: sha512-dz4qCQLurx97FQhnb/EIYTk/ldQ+oafEDUqC0VVIeQS1Q48/YWt/9YNfMmp9SLFqN41ktxny3c8aYxHjmFIB/w==}
    peerDependencies:
      typescript: '>=5.0.4'
      zod: ^3 >=3.19.1
    peerDependenciesMeta:
      typescript:
        optional: true
      zod:
        optional: true
    dependencies:
      typescript: 5.0.2
    dev: false

  /acorn-jsx@5.3.2(acorn@8.8.2):
    resolution: {integrity: sha512-rq9s+JNhf0IChjtDXxllJ7g41oZk5SlXtp0LHwyA5cejwn7vKmKp4pPri6YEePv2PU65sAsegbXtIinmDFDXgQ==}
    peerDependencies:
      acorn: ^6.0.0 || ^7.0.0 || ^8.0.0
    dependencies:
      acorn: 8.8.2
    dev: true

  /acorn@8.8.2:
    resolution: {integrity: sha512-xjIYgE8HBrkpd/sJqOGNspf8uHG+NOHGOw6a/Urj8taM2EXfdNAH2oFcPeIFfsv3+kz/mJrS5VuMqbNLjCa2vw==}
    engines: {node: '>=0.4.0'}
    hasBin: true
    dev: true

  /aes-js@3.1.2:
    resolution: {integrity: sha512-e5pEa2kBnBOgR4Y/p20pskXI74UEz7de8ZGVo58asOtvSVG5YAbJeELPZxOmt+Bnz3rX753YKhfIn4X4l1PPRQ==}
    dev: false

  /agentkeepalive@4.3.0:
    resolution: {integrity: sha512-7Epl1Blf4Sy37j4v9f9FjICCh4+KAQOyXgHEwlyBiAQLbhKdq/i2QQU3amQalS/wPhdPzDXPL5DMR5bkn+YeWg==}
    engines: {node: '>= 8.0.0'}
    dependencies:
      debug: 4.3.4
      depd: 2.0.0
      humanize-ms: 1.2.1
    transitivePeerDependencies:
      - supports-color
    dev: false

  /ahocorasick@1.0.2:
    resolution: {integrity: sha512-hCOfMzbFx5IDutmWLAt6MZwOUjIfSM9G9FyVxytmE4Rs/5YDPWQrD/+IR1w+FweD9H2oOZEnv36TmkjhNURBVA==}
    dev: false

  /ajv@6.12.6:
    resolution: {integrity: sha512-j3fVLgvTo527anyYyJOGTYJbG+vnnQYvE0m5mmkc1TK+nxAppkCLMIL0aZ4dblVCNoGShhm+kzE4ZUykBoMg4g==}
    dependencies:
      fast-deep-equal: 3.1.3
      fast-json-stable-stringify: 2.1.0
      json-schema-traverse: 0.4.1
      uri-js: 4.4.1
    dev: true

  /animated-number-react@0.1.2(react-dom@18.2.0)(react@18.2.0):
    resolution: {integrity: sha512-NsocKXtCKk0cBFITS8lGxRo02QGr4LQLh61S1KUkeEpn30H3fj0Tqz/XSyJeZ6JLJMWOP/8MV/us2Xj9I8DnVw==}
    peerDependencies:
      react: '>=0.14'
      react-dom: '>=0.14'
    dependencies:
      prop-types: 15.8.1
      react: 18.2.0
      react-dom: 18.2.0(react@18.2.0)
    dev: false

  /ansi-regex@5.0.1:
    resolution: {integrity: sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==}
    engines: {node: '>=8'}

  /ansi-styles@3.2.1:
    resolution: {integrity: sha512-VT0ZI6kZRdTh8YyJw3SMbYm/u+NqfsAxEpWO0Pf9sq8/e94WxxOpPKx9FR1FlyCtOVDNOQ+8ntlqFxiRc+r5qA==}
    engines: {node: '>=4'}
    dependencies:
      color-convert: 1.9.3
    dev: true

  /ansi-styles@4.3.0:
    resolution: {integrity: sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==}
    engines: {node: '>=8'}
    dependencies:
      color-convert: 2.0.1

  /anymatch@3.1.3:
    resolution: {integrity: sha512-KMReFUr0B4t+D+OBkjR3KYqvocp2XaSzO55UcB6mgQMd3KbcE+mWTyvVV7D/zsdEbNnV6acZUutkiHQXvTr1Rw==}
    engines: {node: '>= 8'}
    dependencies:
      normalize-path: 3.0.0
      picomatch: 2.3.1
    dev: true

  /argparse@2.0.1:
    resolution: {integrity: sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q==}
    dev: true

  /array-union@2.1.0:
    resolution: {integrity: sha512-HGyxoOTYUyCM6stUe6EJgnd4EoewAI7zMdfqO+kGjnlZmBDz/cR5pf8r/cR4Wq60sL/p0IkcjUEEPwS3GFrIyw==}
    engines: {node: '>=8'}
    dev: true

  /async-mutex@0.2.6:
    resolution: {integrity: sha512-Hs4R+4SPgamu6rSGW8C7cV9gaWUKEHykfzCCvIRuaVv636Ju10ZdeUbvb4TBEW0INuq2DHZqXbK4Nd3yG4RaRw==}
    dependencies:
      tslib: 2.6.0
    dev: false

  /atomic-sleep@1.0.0:
    resolution: {integrity: sha512-kNOjDqAh7px0XWNI+4QbzoiR/nTkHAWNud2uvnJquD1/x5a7EQZMJT0AczqK0Qn67oY/TTQ1LbUKajZpp3I9tQ==}
    engines: {node: '>=8.0.0'}
    dev: false

  /available-typed-arrays@1.0.5:
    resolution: {integrity: sha512-DMD0KiN46eipeziST1LPP/STfDU0sufISXmjSgvVsoU2tqxctQeASejWcfNtxYKqETM1UxQ8sp2OrSBWpHY6sw==}
    engines: {node: '>= 0.4'}
    dev: false

  /balanced-match@1.0.2:
    resolution: {integrity: sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==}
    dev: true

  /base-x@3.0.9:
    resolution: {integrity: sha512-H7JU6iBHTal1gp56aKoaa//YUxEaAOUiydvrV/pILqIHXTtqxSkATOnDA2u+jZ/61sD+L/412+7kzXRtWukhpQ==}
    dependencies:
      safe-buffer: 5.2.1
    dev: false

  /base64-js@1.5.1:
    resolution: {integrity: sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA==}
    dev: false

  /bigint-buffer@1.1.5:
    resolution: {integrity: sha512-trfYco6AoZ+rKhKnxA0hgX0HAbVP/s808/EuDSe2JDzUnCp/xAsli35Orvk67UrTEcwuxZqYZDmfA2RXJgxVvA==}
    engines: {node: '>= 10.0.0'}
    requiresBuild: true
    dependencies:
      bindings: 1.5.0
    dev: false

  /binary-extensions@2.2.0:
    resolution: {integrity: sha512-jDctJ/IVQbZoJykoeHbhXpOlNBqGNcwXJKJog42E5HDPUwQTSdjCHdihjj0DlnheQ7blbT6dHOafNAiS8ooQKA==}
    engines: {node: '>=8'}
    dev: true

  /bind-decorator@1.0.11:
    resolution: {integrity: sha512-yzkH0uog6Vv/vQ9+rhSKxecnqGUZHYncg7qS7voz3Q76+TAi1SGiOKk2mlOvusQnFz9Dc4BC/NMkeXu11YgjJg==}
    dev: false

  /bindings@1.5.0:
    resolution: {integrity: sha512-p2q/t/mhvuOj/UeLlV6566GD/guowlr0hHxClI0W9m7MWYkL1F0hLo+0Aexs9HSPCtR1SXQ0TD3MMKrXZajbiQ==}
    dependencies:
      file-uri-to-path: 1.0.0
    dev: false

  /bn.js@5.2.1:
    resolution: {integrity: sha512-eXRvHzWyYPBuB4NBy0cmYQjGitUrtqwbvlzP3G6VFnNRbsZQIxQ10PbKKHt8gZ/HW/D/747aDl+QkDqg3KQLMQ==}
    dev: false

  /borsh@0.7.0:
    resolution: {integrity: sha512-CLCsZGIBCFnPtkNnieW/a8wmreDmfUtjU2m9yHrzPXIlNbqVs0AQrSatSG6vdNYUqdc83tkQi2eHfF98ubzQLA==}
    dependencies:
      bn.js: 5.2.1
      bs58: 4.0.1
      text-encoding-utf-8: 1.0.2
    dev: false

  /brace-expansion@1.1.11:
    resolution: {integrity: sha512-iCuPHDFgrHX7H2vEI/5xpz07zSHB00TpugqhmYtVmMO6518mCuRMoOYFldEBl0g187ufozdaHgWKcYFb61qGiA==}
    dependencies:
      balanced-match: 1.0.2
      concat-map: 0.0.1
    dev: true

  /braces@3.0.2:
    resolution: {integrity: sha512-b8um+L1RzM3WDSzvhm6gIz1yfTbBt6YTlcEKAvsmqCZZFw46z626lVj9j1yEPW33H5H+lBQpZMP1k8l+78Ha0A==}
    engines: {node: '>=8'}
    dependencies:
      fill-range: 7.0.1
    dev: true

  /browserslist@4.21.7:
    resolution: {integrity: sha512-BauCXrQ7I2ftSqd2mvKHGo85XR0u7Ru3C/Hxsy/0TkfCtjrmAbPdzLGasmoiBxplpDXlPvdjX9u7srIMfgasNA==}
    engines: {node: ^6 || ^7 || ^8 || ^9 || ^10 || ^11 || ^12 || >=13.7}
    hasBin: true
    dependencies:
      caniuse-lite: 1.0.30001495
      electron-to-chromium: 1.4.425
      node-releases: 2.0.12
      update-browserslist-db: 1.0.11(browserslist@4.21.7)
    dev: true

  /bs58@4.0.1:
    resolution: {integrity: sha512-Ok3Wdf5vOIlBrgCvTq96gBkJw+JUEzdBgyaza5HLtPm7yTHkjRy8+JzNyHF7BHa0bNWOQIp3m5YF0nnFcOIKLw==}
    dependencies:
      base-x: 3.0.9
    dev: false

  /buffer@6.0.3:
    resolution: {integrity: sha512-FTiCpNxtwiZZHEZbcbTIcZjERVICn9yq/pDFkTl95/AxzD1naBctN7YO68riM/gLSDY7sdrMby8hofADYuuqOA==}
    dependencies:
      base64-js: 1.5.1
      ieee754: 1.2.1
    dev: false

  /bufferutil@4.0.7:
    resolution: {integrity: sha512-kukuqc39WOHtdxtw4UScxF/WVnMFVSQVKhtx3AjZJzhd0RGZZldcrfSEbVsWWe6KNH253574cq5F+wpv0G9pJw==}
    engines: {node: '>=6.14.2'}
    requiresBuild: true
    dependencies:
      node-gyp-build: 4.6.0
    dev: false

  /call-bind@1.0.2:
    resolution: {integrity: sha512-7O+FbCihrB5WGbFYesctwmTKae6rOiIzmz1icreWJ+0aA7LJfuqhEso2T9ncpcFtzMQtzXf2QGGueWJGTYsqrA==}
    dependencies:
      function-bind: 1.1.1
      get-intrinsic: 1.2.1
    dev: false

  /callsites@3.1.0:
    resolution: {integrity: sha512-P8BjAsXvZS+VIDUI11hHCQEv74YT67YUi5JJFNWIqL235sBmjX4+qx9Muvls5ivyNENctx46xQLQ3aTuE7ssaQ==}
    engines: {node: '>=6'}
    dev: true

  /camelcase@5.3.1:
    resolution: {integrity: sha512-L28STB170nwWS63UjtlEOE3dldQApaJXZkOI1uMFfzf3rRuPegHaHesyee+YxQ+W6SvRDQV6UrdOdRiR153wJg==}
    engines: {node: '>=6'}
    dev: false

  /caniuse-lite@1.0.30001495:
    resolution: {integrity: sha512-F6x5IEuigtUfU5ZMQK2jsy5JqUUlEFRVZq8bO2a+ysq5K7jD6PPc9YXZj78xDNS3uNchesp1Jw47YXEqr+Viyg==}
    dev: true

  /chalk@2.4.2:
    resolution: {integrity: sha512-Mti+f9lpJNcwF4tWV8/OrTTtF1gZi+f8FqlyAdouralcFWFQWF2+NgCHShjkCb+IFBLq9buZwE1xckQU4peSuQ==}
    engines: {node: '>=4'}
    dependencies:
      ansi-styles: 3.2.1
      escape-string-regexp: 1.0.5
      supports-color: 5.5.0
    dev: true

  /chalk@4.1.2:
    resolution: {integrity: sha512-oKnbhFyRIXpUuez8iBMmyEa4nbj4IOQyuhc/wy9kY7/WVPcwIO9VA668Pu8RkO7+0G76SLROeyw9CpQ061i4mA==}
    engines: {node: '>=10'}
    dependencies:
      ansi-styles: 4.3.0
      supports-color: 7.2.0

  /chokidar@3.5.3:
    resolution: {integrity: sha512-Dr3sfKRP6oTcjf2JmUmFJfeVMvXBdegxB0iVQ5eb2V10uFJUCAS8OByZdVAyVb8xXNz3GjjTgj9kLWsZTqE6kw==}
    engines: {node: '>= 8.10.0'}
    dependencies:
      anymatch: 3.1.3
      braces: 3.0.2
      glob-parent: 5.1.2
      is-binary-path: 2.1.0
      is-glob: 4.0.3
      normalize-path: 3.0.0
      readdirp: 3.6.0
    optionalDependencies:
      fsevents: 2.3.2
    dev: true

  /client-only@0.0.1:
    resolution: {integrity: sha512-IV3Ou0jSMzZrd3pZ48nLkT9DA7Ag1pnPzaiQhpW7c3RbcqqzvzzVu+L8gfqMp/8IM2MQtSiqaCxrrcfu8I8rMA==}
    dev: false

  /cliui@6.0.0:
    resolution: {integrity: sha512-t6wbgtoCXvAzst7QgXxJYqPt0usEfbgQdftEPbLL/cvv6HPE5VgvqCuAIDR0NgU52ds6rFwqrgakNLrHEjCbrQ==}
    dependencies:
      string-width: 4.2.3
      strip-ansi: 6.0.1
      wrap-ansi: 6.2.0
    dev: false

  /clsx@1.1.1:
    resolution: {integrity: sha512-6/bPho624p3S2pMyvP5kKBPXnI3ufHLObBFCfgx+LkeR5lg2XYy2hqZqUf45ypD8COn2bhgGJSUE+l5dhNBieA==}
    engines: {node: '>=6'}
    dev: false

  /clsx@1.2.1:
    resolution: {integrity: sha512-EcR6r5a8bj6pu3ycsa/E/cKVGuTgZJZdsyUYHOksG/UHIiKfjxzRxYJpyVBwYaQeOvghal9fcc4PidlgzugAQg==}
    engines: {node: '>=6'}
    dev: false

  /color-convert@1.9.3:
    resolution: {integrity: sha512-QfAUtd+vFdAtFQcC8CCyYt1fYWxSqAiK2cSD6zDB8N3cpsEBAvRxp9zOGg6G/SHHJYAT88/az/IuDGALsNVbGg==}
    dependencies:
      color-name: 1.1.3
    dev: true

  /color-convert@2.0.1:
    resolution: {integrity: sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==}
    engines: {node: '>=7.0.0'}
    dependencies:
      color-name: 1.1.4

  /color-name@1.1.3:
    resolution: {integrity: sha512-72fSenhMw2HZMTVHeCA9KCmpEIbzWiQsjN+BHcBbS9vr1mtt+vJjPdksIBNUmKAW8TFUDPJK5SUU3QhE9NEXDw==}
    dev: true

  /color-name@1.1.4:
    resolution: {integrity: sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==}

  /commander@2.20.3:
    resolution: {integrity: sha512-GpVkmM8vF2vQUkj2LvZmD35JxeJOLCwJ9cUkugyk2nuhbv3+mJvpLYYt+0+USMxE+oj+ey/lJEnhZw75x/OMcQ==}
    dev: false

  /concat-map@0.0.1:
    resolution: {integrity: sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKnVxw2bCFMRljaA7EXHaXZ8wsHdodFvbkhKmqg==}
    dev: true

  /convert-source-map@1.9.0:
    resolution: {integrity: sha512-ASFBup0Mz1uyiIjANan1jzLQami9z1PoYSZCiiYW2FczPbenXc45FZdBZLzOT+r6+iciuEModtmCti+hjaAk0A==}
    dev: true

  /copy-to-clipboard@3.3.3:
    resolution: {integrity: sha512-2KV8NhB5JqC3ky0r9PMCAZKbUHSwtEo4CwCs0KXgruG43gX5PMqDEBbVU4OUzw2MuAWUfsuFmWvEKG5QRfSnJA==}
    dependencies:
      toggle-selection: 1.0.6
    dev: false

  /cross-fetch@3.1.8:
    resolution: {integrity: sha512-cvA+JwZoU0Xq+h6WkMvAUqPEYy92Obet6UdKLfW60qn99ftItKjB5T+BkyWOFWe2pUyfQ+IJHmpOTznqk1M6Kg==}
    dependencies:
      node-fetch: 2.6.12
    transitivePeerDependencies:
      - encoding
    dev: false

  /cross-spawn@7.0.3:
    resolution: {integrity: sha512-iRDPJKUPVEND7dHPO8rkbOnPpyDygcDFtWjpeWNCgy8WP2rXcxXL8TskReQl6OrB2G7+UJrags1q15Fudc7G6w==}
    engines: {node: '>= 8'}
    dependencies:
      path-key: 3.1.1
      shebang-command: 2.0.0
      which: 2.0.2
    dev: true

  /css-what@5.1.0:
    resolution: {integrity: sha512-arSMRWIIFY0hV8pIxZMEfmMI47Wj3R/aWpZDDxWYCPEiOMv6tfOrnpDtgxBYPEQD4V0Y/958+1TdC3iWTFcUPw==}
    engines: {node: '>= 6'}
    dev: false

  /cssesc@3.0.0:
    resolution: {integrity: sha512-/Tb/JcjK111nNScGob5MNtsntNM1aCNUDipB/TkwZFhyDrrE47SOx/18wF2bbjgc3ZzCSKW1T5nt5EbFoAz/Vg==}
    engines: {node: '>=4'}
    hasBin: true
    dev: false

  /csstype@3.1.2:
    resolution: {integrity: sha512-I7K1Uu0MBPzaFKg4nI5Q7Vs2t+3gWWW648spaF+Rg7pI9ds18Ugn+lvg4SHczUdKlHI5LWBXyqfS8+DufyBsgQ==}

  /debug@4.3.4:
    resolution: {integrity: sha512-PRWFHuSU3eDtQJPvnNY7Jcket1j0t5OuOsFzPPzsekD52Zl8qUfFIPEiswXqIvHWGVHOgX+7G/vCNNhehwxfkQ==}
    engines: {node: '>=6.0'}
    peerDependencies:
      supports-color: '*'
    peerDependenciesMeta:
      supports-color:
        optional: true
    dependencies:
      ms: 2.1.2

  /decamelize@1.2.0:
    resolution: {integrity: sha512-z2S+W9X73hAUUki+N+9Za2lBlun89zigOyGrsax+KUQ6wKW4ZoWpEYBkGhQjwAjjDCkWxhY0VKEhk8wzY7F5cA==}
    engines: {node: '>=0.10.0'}
    dev: false

  /decode-uri-component@0.2.2:
    resolution: {integrity: sha512-FqUYQ+8o158GyGTrMFJms9qh3CqTKvAqgqsTnkLI8sKu0028orqBhxNMFkFen0zGyg6epACD32pjVk58ngIErQ==}
    engines: {node: '>=0.10'}
    dev: false

  /deep-is@0.1.4:
    resolution: {integrity: sha512-oIPzksmTg4/MriiaYGO+okXDT7ztn/w3Eptv/+gSIdMdKsJo0u4CfYNFJPy+4SKMuCqGw2wxnA+URMg3t8a/bQ==}
    dev: true

  /deep-object-diff@1.1.9:
    resolution: {integrity: sha512-Rn+RuwkmkDwCi2/oXOFS9Gsr5lJZu/yTGpK7wAaAIE75CC+LCGEZHpY6VQJa/RoJcrmaA/docWJZvYohlNkWPA==}
    dev: false

  /deepmerge@4.3.1:
    resolution: {integrity: sha512-3sUqbMEc77XqpdNO7FRyRog+eW3ph+GYCbj+rK+uYyRMuwsVy0rMiVtPn+QJlKFvWP/1PYpapqYn0Me2knFn+A==}
    engines: {node: '>=0.10.0'}
    dev: false

  /delay@5.0.0:
    resolution: {integrity: sha512-ReEBKkIfe4ya47wlPYf/gu5ib6yUG0/Aez0JQZQz94kiWtRQvZIQbTiehsnwHvLSWJnQdhVeqYue7Id1dKr0qw==}
    engines: {node: '>=10'}
    dev: false

  /depd@2.0.0:
    resolution: {integrity: sha512-g7nH6P6dyDioJogAAGprGpCtVImJhpPk/roCzdb3fIh61/s/nPsfR6onyMwkCAR/OlC3yBC0lESvUoQEAssIrw==}
    engines: {node: '>= 0.8'}
    dev: false

  /detect-browser@5.3.0:
    resolution: {integrity: sha512-53rsFbGdwMwlF7qvCt0ypLM5V5/Mbl0szB7GPN8y9NCcbknYOeVVXdrXEq+90IwAfrrzt6Hd+u2E2ntakICU8w==}
    dev: false

  /detect-node-es@1.1.0:
    resolution: {integrity: sha512-ypdmJU/TbBby2Dxibuv7ZLW3Bs1QEmM7nHjEANfohJLvE0XVujisn1qPJcZxg+qDucsr+bP6fLD1rPS3AhJ7EQ==}
    dev: false

  /dijkstrajs@1.0.3:
    resolution: {integrity: sha512-qiSlmBq9+BCdCA/L46dw8Uy93mloxsPSbwnm5yrKn2vMPiy8KyAskTF6zuV/j5BMsmOGZDPs7KjU+mjb670kfA==}
    dev: false

  /dir-glob@3.0.1:
    resolution: {integrity: sha512-WkrWp9GR4KXfKGYzOLmTuGVi1UWFfws377n9cc55/tb6DuqyF6pcQ5AbiHEshaDpY9v6oaSr2XCDidGmMwdzIA==}
    engines: {node: '>=8'}
    dependencies:
      path-type: 4.0.0
    dev: true

  /doctrine@3.0.0:
    resolution: {integrity: sha512-yS+Q5i3hBf7GBkd4KG8a7eBNNWNGLTaEwwYWUijIYM7zrlYDM0BFXHjjPWlWZ1Rg7UaddZeIDmi9jF3HmqiQ2w==}
    engines: {node: '>=6.0.0'}
    dependencies:
      esutils: 2.0.3
    dev: true

  /duplexify@4.1.2:
    resolution: {integrity: sha512-fz3OjcNCHmRP12MJoZMPglx8m4rrFP8rovnk4vT8Fs+aonZoCwGg10dSsQsfP/E62eZcPTMSMP6686fu9Qlqtw==}
    dependencies:
      end-of-stream: 1.4.4
      inherits: 2.0.4
      readable-stream: 3.6.2
      stream-shift: 1.0.1
    dev: false

  /electron-to-chromium@1.4.425:
    resolution: {integrity: sha512-wv1NufHxu11zfDbY4fglYQApMswleE9FL/DSeyOyauVXDZ+Kco96JK/tPfBUaDqfRarYp2WH2hJ/5UnVywp9Jg==}
    dev: true

  /emoji-regex@8.0.0:
    resolution: {integrity: sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==}
    dev: false

  /encode-utf8@1.0.3:
    resolution: {integrity: sha512-ucAnuBEhUK4boH2HjVYG5Q2mQyPorvv0u/ocS+zhdw0S8AlHYY+GOFhP1Gio5z4icpP2ivFSvhtFjQi8+T9ppw==}
    dev: false

  /end-of-stream@1.4.4:
    resolution: {integrity: sha512-+uw1inIHVPQoaVuHzRyXd21icM+cnt4CzD5rW+NC1wjOUSTOs+Te7FOv7AhN7vS9x/oIyhLP5PR1H+phQAHu5Q==}
    dependencies:
      once: 1.4.0
    dev: false

  /es6-promise@4.2.8:
    resolution: {integrity: sha512-HJDGx5daxeIvxdBxvG2cb9g4tEvwIk3i8+nhX0yGrYmZUzbkdg8QbDevheDB8gd0//uPj4c1EQua8Q+MViT0/w==}
    dev: false

  /es6-promisify@5.0.0:
    resolution: {integrity: sha512-C+d6UdsYDk0lMebHNR4S2NybQMMngAOnOwYBQjTOiv0MkoJMP0Myw2mgpDLBcpfCmRLxyFqYhS/CfOENq4SJhQ==}
    dependencies:
      es6-promise: 4.2.8
    dev: false

  /esbuild@0.17.19:
    resolution: {integrity: sha512-XQ0jAPFkK/u3LcVRcvVHQcTIqD6E2H1fvZMA5dQPSOWb3suUbWbfbRf94pjc0bNzRYLfIrDRQXr7X+LHIm5oHw==}
    engines: {node: '>=12'}
    hasBin: true
    requiresBuild: true
    optionalDependencies:
      '@esbuild/android-arm': 0.17.19
      '@esbuild/android-arm64': 0.17.19
      '@esbuild/android-x64': 0.17.19
      '@esbuild/darwin-arm64': 0.17.19
      '@esbuild/darwin-x64': 0.17.19
      '@esbuild/freebsd-arm64': 0.17.19
      '@esbuild/freebsd-x64': 0.17.19
      '@esbuild/linux-arm': 0.17.19
      '@esbuild/linux-arm64': 0.17.19
      '@esbuild/linux-ia32': 0.17.19
      '@esbuild/linux-loong64': 0.17.19
      '@esbuild/linux-mips64el': 0.17.19
      '@esbuild/linux-ppc64': 0.17.19
      '@esbuild/linux-riscv64': 0.17.19
      '@esbuild/linux-s390x': 0.17.19
      '@esbuild/linux-x64': 0.17.19
      '@esbuild/netbsd-x64': 0.17.19
      '@esbuild/openbsd-x64': 0.17.19
      '@esbuild/sunos-x64': 0.17.19
      '@esbuild/win32-arm64': 0.17.19
      '@esbuild/win32-ia32': 0.17.19
      '@esbuild/win32-x64': 0.17.19
    dev: true

  /escalade@3.1.1:
    resolution: {integrity: sha512-k0er2gUkLf8O0zKJiAhmkTnJlTvINGv7ygDNPbeIsX/TJjGJZHuh9B2UxbsaEkmlEo9MfhrSzmhIlhRlI2GXnw==}
    engines: {node: '>=6'}
    dev: true

  /escape-string-regexp@1.0.5:
    resolution: {integrity: sha512-vbRorB5FUQWvla16U8R/qgaFIya2qGzwDrNmCZuYKrbdSUMG6I1ZCGQRefkRVhuOkIGVne7BQ35DSfo1qvJqFg==}
    engines: {node: '>=0.8.0'}
    dev: true

  /escape-string-regexp@4.0.0:
    resolution: {integrity: sha512-TtpcNJ3XAzx3Gq8sWRzJaVajRs0uVxA2YAkdb1jm2YkPz4G6egUFAyA3n5vtEIZefPk5Wa4UXbKuS5fKkJWdgA==}
    engines: {node: '>=10'}
    dev: true

  /eslint-plugin-react-hooks@4.6.0(eslint@8.38.0):
    resolution: {integrity: sha512-oFc7Itz9Qxh2x4gNHStv3BqJq54ExXmfC+a1NjAta66IAN87Wu0R/QArgIS9qKzX3dXKPI9H5crl9QchNMY9+g==}
    engines: {node: '>=10'}
    peerDependencies:
      eslint: ^3.0.0 || ^4.0.0 || ^5.0.0 || ^6.0.0 || ^7.0.0 || ^8.0.0-0
    dependencies:
      eslint: 8.38.0
    dev: true

  /eslint-plugin-react-refresh@0.3.4(eslint@8.38.0):
    resolution: {integrity: sha512-E0ViBglxSQAERBp6eTj5fPgtCRtDonnbCFiVQBhf4Dto2blJRxg1dFUMdMh7N6ljTI4UwPhHwYDQ3Dyo4m6bwA==}
    peerDependencies:
      eslint: '>=7'
    dependencies:
      eslint: 8.38.0
    dev: true

  /eslint-scope@5.1.1:
    resolution: {integrity: sha512-2NxwbF/hZ0KpepYN0cNbo+FN6XoK7GaHlQhgx/hIZl6Va0bF45RQOOwhLIy8lQDbuCiadSLCBnH2CFYquit5bw==}
    engines: {node: '>=8.0.0'}
    dependencies:
      esrecurse: 4.3.0
      estraverse: 4.3.0
    dev: true

  /eslint-scope@7.2.0:
    resolution: {integrity: sha512-DYj5deGlHBfMt15J7rdtyKNq/Nqlv5KfU4iodrQ019XESsRnwXH9KAE0y3cwtUHDo2ob7CypAnCqefh6vioWRw==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    dependencies:
      esrecurse: 4.3.0
      estraverse: 5.3.0
    dev: true

  /eslint-visitor-keys@3.4.1:
    resolution: {integrity: sha512-pZnmmLwYzf+kWaM/Qgrvpen51upAktaaiI01nsJD/Yr3lMOdNtq0cxkrrg16w64VtisN6okbs7Q8AfGqj4c9fA==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    dev: true

  /eslint@8.38.0:
    resolution: {integrity: sha512-pIdsD2jwlUGf/U38Jv97t8lq6HpaU/G9NKbYmpWpZGw3LdTNhZLbJePqxOXGB5+JEKfOPU/XLxYxFh03nr1KTg==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    hasBin: true
    dependencies:
      '@eslint-community/eslint-utils': 4.4.0(eslint@8.38.0)
      '@eslint-community/regexpp': 4.5.1
      '@eslint/eslintrc': 2.0.3
      '@eslint/js': 8.38.0
      '@humanwhocodes/config-array': 0.11.10
      '@humanwhocodes/module-importer': 1.0.1
      '@nodelib/fs.walk': 1.2.8
      ajv: 6.12.6
      chalk: 4.1.2
      cross-spawn: 7.0.3
      debug: 4.3.4
      doctrine: 3.0.0
      escape-string-regexp: 4.0.0
      eslint-scope: 7.2.0
      eslint-visitor-keys: 3.4.1
      espree: 9.5.2
      esquery: 1.5.0
      esutils: 2.0.3
      fast-deep-equal: 3.1.3
      file-entry-cache: 6.0.1
      find-up: 5.0.0
      glob-parent: 6.0.2
      globals: 13.20.0
      grapheme-splitter: 1.0.4
      ignore: 5.2.4
      import-fresh: 3.3.0
      imurmurhash: 0.1.4
      is-glob: 4.0.3
      is-path-inside: 3.0.3
      js-sdsl: 4.4.1
      js-yaml: 4.1.0
      json-stable-stringify-without-jsonify: 1.0.1
      levn: 0.4.1
      lodash.merge: 4.6.2
      minimatch: 3.1.2
      natural-compare: 1.4.0
      optionator: 0.9.1
      strip-ansi: 6.0.1
      strip-json-comments: 3.1.1
      text-table: 0.2.0
    transitivePeerDependencies:
      - supports-color
    dev: true

  /espree@9.5.2:
    resolution: {integrity: sha512-7OASN1Wma5fum5SrNhFMAMJxOUAbhyfQ8dQ//PJaJbNw0URTPWqIghHWt1MmAANKhHZIYOHruW4Kw4ruUWOdGw==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    dependencies:
      acorn: 8.8.2
      acorn-jsx: 5.3.2(acorn@8.8.2)
      eslint-visitor-keys: 3.4.1
    dev: true

  /esquery@1.5.0:
    resolution: {integrity: sha512-YQLXUplAwJgCydQ78IMJywZCceoqk1oH01OERdSAJc/7U2AylwjhSCLDEtqwg811idIS/9fIU5GjG73IgjKMVg==}
    engines: {node: '>=0.10'}
    dependencies:
      estraverse: 5.3.0
    dev: true

  /esrecurse@4.3.0:
    resolution: {integrity: sha512-KmfKL3b6G+RXvP8N1vr3Tq1kL/oCFgn2NYXEtqP8/L3pKapUA4G8cFVaoF3SU323CD4XypR/ffioHmkti6/Tag==}
    engines: {node: '>=4.0'}
    dependencies:
      estraverse: 5.3.0
    dev: true

  /estraverse@4.3.0:
    resolution: {integrity: sha512-39nnKffWz8xN1BU/2c79n9nB9HDzo0niYUqx6xyqUnyoAnQyyWpOTdZEeiCch8BBu515t4wp9ZmgVfVhn9EBpw==}
    engines: {node: '>=4.0'}
    dev: true

  /estraverse@5.3.0:
    resolution: {integrity: sha512-MMdARuVEQziNTeJD8DgMqmhwR11BRQ/cBP+pLtYdSTnf3MIO8fFeiINEbX36ZdNlfU/7A9f3gUw49B3oQsvwBA==}
    engines: {node: '>=4.0'}
    dev: true

  /esutils@2.0.3:
    resolution: {integrity: sha512-kVscqXk4OCp68SZ0dkgEKVi6/8ij300KBWTJq32P/dYeWTSwK41WyTxalN1eRmA5Z9UU/LX9D7FWSmV9SAYx6g==}
    engines: {node: '>=0.10.0'}
    dev: true

  /eth-block-tracker@6.1.0:
    resolution: {integrity: sha512-K9SY8+/xMBi4M5HHTDdxnpEqEEGjbNpzHFqvxyjMZej8InV/B+CkFRKM6W+uvrFJ7m8Zd1E0qUkseU3vdIDFYQ==}
    engines: {node: '>=14.0.0'}
    dependencies:
      '@metamask/safe-event-emitter': 2.0.0
      '@metamask/utils': 3.6.0
      json-rpc-random-id: 1.0.1
      pify: 3.0.0
    transitivePeerDependencies:
      - supports-color
    dev: false

  /eth-json-rpc-filters@5.1.0:
    resolution: {integrity: sha512-fos+9xmoa1A2Ytsc9eYof17r81BjdJOUcGcgZn4K/tKdCCTb+a8ytEtwlu1op5qsXFDlgGmstTELFrDEc89qEQ==}
    engines: {node: '>=14.0.0'}
    dependencies:
      '@metamask/safe-event-emitter': 2.0.0
      async-mutex: 0.2.6
      eth-query: 2.1.2
      json-rpc-engine: 6.1.0
      pify: 5.0.0
    dev: false

  /eth-query@2.1.2:
    resolution: {integrity: sha512-srES0ZcvwkR/wd5OQBRA1bIJMww1skfGS0s8wlwK3/oNP4+wnds60krvu5R1QbpRQjMmpG5OMIWro5s7gvDPsA==}
    dependencies:
      json-rpc-random-id: 1.0.1
      xtend: 4.0.2
    dev: false

  /eth-rpc-errors@4.0.2:
    resolution: {integrity: sha512-n+Re6Gu8XGyfFy1it0AwbD1x0MUzspQs0D5UiPs1fFPCr6WAwZM+vbIhXheBFrpgosqN9bs5PqlB4Q61U/QytQ==}
    dependencies:
      fast-safe-stringify: 2.1.1
    dev: false

  /eventemitter3@4.0.7:
    resolution: {integrity: sha512-8guHBZCwKnFhYdHr2ysuRWErTwhoN2X8XELRlrRwpmfeY2jjuUN4taQMsULKUVo1K4DvZl+0pgfyoysHxvmvEw==}
    dev: false

  /events@3.3.0:
    resolution: {integrity: sha512-mQw+2fkQbALzQ7V0MY0IqdnXNOeTtP4r0lN9z7AAawCXgqea7bDii20AYrIBrFd/Hx0M2Ocz6S111CaFkUcb0Q==}
    engines: {node: '>=0.8.x'}
    dev: false

  /eyes@0.1.8:
    resolution: {integrity: sha512-GipyPsXO1anza0AOZdy69Im7hGFCNB7Y/NGjDlZGJ3GJJLtwNSb2vrzYrTYJRrRloVx7pl+bhUaTB8yiccPvFQ==}
    engines: {node: '> 0.1.90'}
    dev: false

  /fast-deep-equal@3.1.3:
    resolution: {integrity: sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==}
    dev: true

  /fast-glob@3.2.12:
    resolution: {integrity: sha512-DVj4CQIYYow0BlaelwK1pHl5n5cRSJfM60UA0zK891sVInoPri2Ekj7+e1CT3/3qxXenpI+nBBmQAcJPJgaj4w==}
    engines: {node: '>=8.6.0'}
    dependencies:
      '@nodelib/fs.stat': 2.0.5
      '@nodelib/fs.walk': 1.2.8
      glob-parent: 5.1.2
      merge2: 1.4.1
      micromatch: 4.0.5
    dev: true

  /fast-json-stable-stringify@2.1.0:
    resolution: {integrity: sha512-lhd/wF+Lk98HZoTCtlVraHtfh5XYijIjalXck7saUtuanSDyLMxnHhSXEDJqHxD7msR8D0uCmqlkwjCV8xvwHw==}
    dev: true

  /fast-levenshtein@2.0.6:
    resolution: {integrity: sha512-DCXu6Ifhqcks7TZKY3Hxp3y6qphY5SJZmrWMDrKcERSOXWQdMhU9Ig/PYrzyw/ul9jOIyh0N4M0tbC5hodg8dw==}
    dev: true

  /fast-redact@3.2.0:
    resolution: {integrity: sha512-zaTadChr+NekyzallAMXATXLOR8MNx3zqpZ0MUF2aGf4EathnG0f32VLODNlY8IuGY3HoRO2L6/6fSzNsLaHIw==}
    engines: {node: '>=6'}
    dev: false

  /fast-safe-stringify@2.1.1:
    resolution: {integrity: sha512-W+KJc2dmILlPplD/H4K9l9LcAHAfPtP6BY84uVLXQ6Evcz9Lcg33Y2z1IVblT6xdY54PXYVHEv+0Wpq8Io6zkA==}
    dev: false

  /fast-stable-stringify@1.0.0:
    resolution: {integrity: sha512-wpYMUmFu5f00Sm0cj2pfivpmawLZ0NKdviQ4w9zJeR8JVtOpOxHmLaJuj0vxvGqMJQWyP/COUkF75/57OKyRag==}
    dev: false

  /fastq@1.15.0:
    resolution: {integrity: sha512-wBrocU2LCXXa+lWBt8RoIRD89Fi8OdABODa/kEnyeyjS5aZO5/GNvI5sEINADqP/h8M29UHTHUb53sUu5Ihqdw==}
    dependencies:
      reusify: 1.0.4
    dev: true

  /file-entry-cache@6.0.1:
    resolution: {integrity: sha512-7Gps/XWymbLk2QLYK4NzpMOrYjMhdIxXuIvy2QBsLE6ljuodKvdkWs/cpyJJ3CVIVpH0Oi1Hvg1ovbMzLdFBBg==}
    engines: {node: ^10.12.0 || >=12.0.0}
    dependencies:
      flat-cache: 3.0.4
    dev: true

  /file-uri-to-path@1.0.0:
    resolution: {integrity: sha512-0Zt+s3L7Vf1biwWZ29aARiVYLx7iMGnEUl9x33fbB/j3jR81u/O2LbqK+Bm1CDSNDKVtJ/YjwY7TUd5SkeLQLw==}
    dev: false

  /fill-range@7.0.1:
    resolution: {integrity: sha512-qOo9F+dMUmC2Lcb4BbVvnKJxTPjCm+RRpe4gDuGrzkL7mEVl/djYSu2OdQ2Pa302N4oqkSg9ir6jaLWJ2USVpQ==}
    engines: {node: '>=8'}
    dependencies:
      to-regex-range: 5.0.1
    dev: true

  /filter-obj@1.1.0:
    resolution: {integrity: sha512-8rXg1ZnX7xzy2NGDVkBVaAy+lSlPNwad13BtgSlLuxfIslyt5Vg64U7tFcCt4WS1R0hvtnQybT/IyCkGZ3DpXQ==}
    engines: {node: '>=0.10.0'}
    dev: false

  /find-up@4.1.0:
    resolution: {integrity: sha512-PpOwAdQ/YlXQ2vj8a3h8IipDuYRi3wceVQQGYWxNINccq40Anw7BlsEXCMbt1Zt+OLA6Fq9suIpIWD0OsnISlw==}
    engines: {node: '>=8'}
    dependencies:
      locate-path: 5.0.0
      path-exists: 4.0.0
    dev: false

  /find-up@5.0.0:
    resolution: {integrity: sha512-78/PXT1wlLLDgTzDs7sjq9hzz0vXD+zn+7wypEe4fXQxCmdmqfGsEPQxmiCSQI3ajFV91bVSsvNtrJRiW6nGng==}
    engines: {node: '>=10'}
    dependencies:
      locate-path: 6.0.0
      path-exists: 4.0.0
    dev: true

  /flat-cache@3.0.4:
    resolution: {integrity: sha512-dm9s5Pw7Jc0GvMYbshN6zchCA9RgQlzzEZX3vylR9IqFfS8XciblUXOKfW6SiuJ0e13eDYZoZV5wdrev7P3Nwg==}
    engines: {node: ^10.12.0 || >=12.0.0}
    dependencies:
      flatted: 3.2.7
      rimraf: 3.0.2
    dev: true

  /flatted@3.2.7:
    resolution: {integrity: sha512-5nqDSxl8nn5BSNxyR3n4I6eDmbolI6WT+QqR547RwxQapgjQBmtktdP+HTBb/a/zLsbzERTONyUB5pefh5TtjQ==}
    dev: true

  /for-each@0.3.3:
    resolution: {integrity: sha512-jqYfLp7mo9vIyQf8ykW2v7A+2N4QjeCeI5+Dz9XraiO1ign81wjiH7Fb9vSOWvQfNtmSa4H2RoQTrrXivdUZmw==}
    dependencies:
      is-callable: 1.2.7
    dev: false

  /fs.realpath@1.0.0:
    resolution: {integrity: sha512-OO0pH2lK6a0hZnAdau5ItzHPI6pUlvI7jMVnxUQRtw4owF2wk8lOSabtGDCTP4Ggrg2MbGnWO9X8K1t4+fGMDw==}
    dev: true

  /fsevents@2.3.2:
    resolution: {integrity: sha512-xiqMQR4xAeHTuB9uWm+fFRcIOgKBMiOBP+eXiyT7jsgVCq1bkVygt00oASowB7EdtpOHaaPgKt812P9ab+DDKA==}
    engines: {node: ^8.16.0 || ^10.6.0 || >=11.0.0}
    os: [darwin]
    requiresBuild: true
    dev: true
    optional: true

  /function-bind@1.1.1:
    resolution: {integrity: sha512-yIovAzMX49sF8Yl58fSCWJ5svSLuaibPxXQJFLmBObTuCr0Mf1KiPopGM9NiFjiYBCbfaa2Fh6breQ6ANVTI0A==}
    dev: false

  /gensync@1.0.0-beta.2:
    resolution: {integrity: sha512-3hN7NaskYvMDLQY55gnW3NQ+mesEAepTqlg+VEbj7zzqEMBVNhzcGYYeqFo/TlYz6eQiFcp1HcsCZO+nGgS8zg==}
    engines: {node: '>=6.9.0'}
    dev: true

  /get-caller-file@2.0.5:
    resolution: {integrity: sha512-DyFP3BM/3YHTQOCUL/w0OZHR0lpKeGrxotcHWcqNEdnltqFwXVfhEBQ94eIo34AfQpo0rGki4cyIiftY06h2Fg==}
    engines: {node: 6.* || 8.* || >= 10.*}
    dev: false

  /get-intrinsic@1.2.1:
    resolution: {integrity: sha512-2DcsyfABl+gVHEfCOaTrWgyt+tb6MSEGmKq+kI5HwLbIYgjgmMcV8KQ41uaKz1xxUcn9tJtgFbQUEVcEbd0FYw==}
    dependencies:
      function-bind: 1.1.1
      has: 1.0.3
      has-proto: 1.0.1
      has-symbols: 1.0.3
    dev: false

  /get-nonce@1.0.1:
    resolution: {integrity: sha512-FJhYRoDaiatfEkUK8HKlicmu/3SGFD51q3itKDGoSTysQJBnfOcxU5GxnhE1E6soB76MbT0MBtnKJuXyAx+96Q==}
    engines: {node: '>=6'}
    dev: false

  /glob-parent@5.1.2:
    resolution: {integrity: sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==}
    engines: {node: '>= 6'}
    dependencies:
      is-glob: 4.0.3
    dev: true

  /glob-parent@6.0.2:
    resolution: {integrity: sha512-XxwI8EOhVQgWp6iDL+3b0r86f4d6AX6zSU55HfB4ydCEuXLXc5FcYeOu+nnGftS4TEju/11rt4KJPTMgbfmv4A==}
    engines: {node: '>=10.13.0'}
    dependencies:
      is-glob: 4.0.3
    dev: true

  /glob@7.2.3:
    resolution: {integrity: sha512-nFR0zLpU2YCaRxwoCJvL6UvCH2JFyFVIvwTLsIf21AuHlMskA1hhTdk+LlYJtOlYt9v6dvszD2BGRqBL+iQK9Q==}
    dependencies:
      fs.realpath: 1.0.0
      inflight: 1.0.6
      inherits: 2.0.4
      minimatch: 3.1.2
      once: 1.4.0
      path-is-absolute: 1.0.1
    dev: true

  /globals@11.12.0:
    resolution: {integrity: sha512-WOBp/EEGUiIsJSp7wcv/y6MO+lV9UoncWqxuFfm8eBwzWNgyfBd6Gz+IeKQ9jCmyhoH99g15M3T+QaVHFjizVA==}
    engines: {node: '>=4'}
    dev: true

  /globals@13.20.0:
    resolution: {integrity: sha512-Qg5QtVkCy/kv3FUSlu4ukeZDVf9ee0iXLAUYX13gbR17bnejFTzr4iS9bY7kwCf1NztRNm1t91fjOiyx4CSwPQ==}
    engines: {node: '>=8'}
    dependencies:
      type-fest: 0.20.2
    dev: true

  /globby@11.1.0:
    resolution: {integrity: sha512-jhIXaOzy1sb8IyocaruWSn1TjmnBVs8Ayhcy83rmxNJ8q2uWKCAj3CnJY+KpGSXCueAPc0i05kVvVKtP1t9S3g==}
    engines: {node: '>=10'}
    dependencies:
      array-union: 2.1.0
      dir-glob: 3.0.1
      fast-glob: 3.2.12
      ignore: 5.2.4
      merge2: 1.4.1
      slash: 3.0.0
    dev: true

  /gopd@1.0.1:
    resolution: {integrity: sha512-d65bNlIadxvpb/A2abVdlqKqV563juRnZ1Wtk6s1sIR8uNsXR70xqIzVqxVf1eTqDunwT2MkczEeaezCKTZhwA==}
    dependencies:
      get-intrinsic: 1.2.1
    dev: false

  /grapheme-splitter@1.0.4:
    resolution: {integrity: sha512-bzh50DW9kTPM00T8y4o8vQg89Di9oLJVLW/KaOGIXJWP/iqCN6WKYkbNOF04vFLJhwcpYUh9ydh/+5vpOqV4YQ==}
    dev: true

  /has-flag@3.0.0:
    resolution: {integrity: sha512-sKJf1+ceQBr4SMkvQnBDNDtf4TXpVhVGateu0t918bl30FnbE2m4vNLX+VWe/dpjlb+HugGYzW7uQXH98HPEYw==}
    engines: {node: '>=4'}
    dev: true

  /has-flag@4.0.0:
    resolution: {integrity: sha512-EykJT/Q1KjTWctppgIAgfSO0tKVuZUjhgMr17kqTumMl6Afv3EISleU7qZUzoXDFTAHTDC4NOoG/ZxU3EvlMPQ==}
    engines: {node: '>=8'}

  /has-proto@1.0.1:
    resolution: {integrity: sha512-7qE+iP+O+bgF9clE5+UoBFzE65mlBiVj3tKCrlNQ0Ogwm0BjpT/gK4SlLYDMybDh5I3TCTKnPPa0oMG7JDYrhg==}
    engines: {node: '>= 0.4'}
    dev: false

  /has-symbols@1.0.3:
    resolution: {integrity: sha512-l3LCuF6MgDNwTDKkdYGEihYjt5pRPbEg46rtlmnSPlUbgmB8LOIrKJbYYFBSbnPaJexMKtiPO8hmeRjRz2Td+A==}
    engines: {node: '>= 0.4'}
    dev: false

  /has-tostringtag@1.0.0:
    resolution: {integrity: sha512-kFjcSNhnlGV1kyoGk7OXKSawH5JOb/LzUc5w9B02hOTO0dfFRjbHQKvg1d6cf3HbeUmtU9VbbV3qzZ2Teh97WQ==}
    engines: {node: '>= 0.4'}
    dependencies:
      has-symbols: 1.0.3
    dev: false

  /has@1.0.3:
    resolution: {integrity: sha512-f2dvO0VU6Oej7RkWJGrehjbzMAjFp5/VKPp5tTpWIV4JHHZK1/BxbFRtf/siA2SWTe09caDmVtYYzWEIbBS4zw==}
    engines: {node: '>= 0.4.0'}
    dependencies:
      function-bind: 1.1.1
    dev: false

  /hash.js@1.1.7:
    resolution: {integrity: sha512-taOaskGt4z4SOANNseOviYDvjEJinIkRgmp7LbKP2YTTmVxWBl87s/uzK9r+44BclBSp2X7K1hqeNfz9JbBeXA==}
    dependencies:
      inherits: 2.0.4
      minimalistic-assert: 1.0.1
    dev: false

  /hey-listen@1.0.8:
    resolution: {integrity: sha512-COpmrF2NOg4TBWUJ5UVyaCU2A88wEMkUPK4hNqyCkqHbxT92BbvfjoSozkAIIm6XhicGlJHhFdullInrdhwU8Q==}
    dev: false

  /humanize-ms@1.2.1:
    resolution: {integrity: sha512-Fl70vYtsAFb/C06PTS9dZBo7ihau+Tu/DNCk/OyHhea07S+aeMWpFFkUaXRa8fI+ScZbEI8dfSxwY7gxZ9SAVQ==}
    dependencies:
      ms: 2.1.2
    dev: false

  /ieee754@1.2.1:
    resolution: {integrity: sha512-dcyqhDvX1C46lXZcVqCpK+FtMRQVdIMN6/Df5js2zouUsqG7I6sFxitIC+7KYK29KdXOLHdu9zL4sFnoVQnqaA==}
    dev: false

  /ignore@5.2.4:
    resolution: {integrity: sha512-MAb38BcSbH0eHNBxn7ql2NH/kX33OkB3lZ1BNdh7ENeRChHTYsTvWrMubiIAMNS2llXEEgZ1MUOBtXChP3kaFQ==}
    engines: {node: '>= 4'}
    dev: true

  /immutable@4.3.0:
    resolution: {integrity: sha512-0AOCmOip+xgJwEVTQj1EfiDDOkPmuyllDuTuEX+DDXUgapLAsBIfkg3sxCYyCEA8mQqZrrxPUGjcOQ2JS3WLkg==}
    dev: true

  /import-fresh@3.3.0:
    resolution: {integrity: sha512-veYYhQa+D1QBKznvhUHxb8faxlrwUnxseDAbAp457E0wLNio2bOSKnjYDhMj+YiAq61xrMGhQk9iXVk5FzgQMw==}
    engines: {node: '>=6'}
    dependencies:
      parent-module: 1.0.1
      resolve-from: 4.0.0
    dev: true

  /imurmurhash@0.1.4:
    resolution: {integrity: sha512-JmXMZ6wuvDmLiHEml9ykzqO6lwFbof0GG4IkcGaENdCRDDmMVnny7s5HsIgHCbaq0w2MyPhDqkhTUgS2LU2PHA==}
    engines: {node: '>=0.8.19'}
    dev: true

  /inflight@1.0.6:
    resolution: {integrity: sha512-k92I/b08q4wvFscXCLvqfsHCrjrF7yiXsQuIVvVE7N82W3+aqpzuUdBbfhWcy/FZR3/4IgflMgKLOsvPDrGCJA==}
    dependencies:
      once: 1.4.0
      wrappy: 1.0.2
    dev: true

  /inherits@2.0.4:
    resolution: {integrity: sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==}

  /invariant@2.2.4:
    resolution: {integrity: sha512-phJfQVBuaJM5raOpJjSfkiD6BpbCE4Ns//LaXl6wGYtUBY83nWS6Rf9tXm2e8VaK60JEjYldbPif/A2B1C2gNA==}
    dependencies:
      loose-envify: 1.4.0
    dev: false

  /is-arguments@1.1.1:
    resolution: {integrity: sha512-8Q7EARjzEnKpt/PCD7e1cgUS0a6X8u5tdSiMqXhojOdoV9TsMsiO+9VLC5vAmO8N7/GmXn7yjR8qnA6bVAEzfA==}
    engines: {node: '>= 0.4'}
    dependencies:
      call-bind: 1.0.2
      has-tostringtag: 1.0.0
    dev: false

  /is-binary-path@2.1.0:
    resolution: {integrity: sha512-ZMERYes6pDydyuGidse7OsHxtbI7WVeUEozgR/g7rd0xUimYNlvZRE/K2MgZTjWy725IfelLeVcEM97mmtRGXw==}
    engines: {node: '>=8'}
    dependencies:
      binary-extensions: 2.2.0
    dev: true

  /is-callable@1.2.7:
    resolution: {integrity: sha512-1BC0BVFhS/p0qtw6enp8e+8OD0UrK0oFLztSjNzhcKA3WDuJxxAPXzPuPtKkjEY9UUoEWlX/8fgKeu2S8i9JTA==}
    engines: {node: '>= 0.4'}
    dev: false

  /is-extglob@2.1.1:
    resolution: {integrity: sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==}
    engines: {node: '>=0.10.0'}
    dev: true

  /is-fullwidth-code-point@3.0.0:
    resolution: {integrity: sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==}
    engines: {node: '>=8'}
    dev: false

  /is-generator-function@1.0.10:
    resolution: {integrity: sha512-jsEjy9l3yiXEQ+PsXdmBwEPcOxaXWLspKdplFUVI9vq1iZgIekeC0L167qeu86czQaxed3q/Uzuw0swL0irL8A==}
    engines: {node: '>= 0.4'}
    dependencies:
      has-tostringtag: 1.0.0
    dev: false

  /is-glob@4.0.3:
    resolution: {integrity: sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==}
    engines: {node: '>=0.10.0'}
    dependencies:
      is-extglob: 2.1.1
    dev: true

  /is-number@7.0.0:
    resolution: {integrity: sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==}
    engines: {node: '>=0.12.0'}
    dev: true

  /is-path-inside@3.0.3:
    resolution: {integrity: sha512-Fd4gABb+ycGAmKou8eMftCupSir5lRxqf4aD/vd0cD2qc4HL07OjCeuHMr8Ro4CoMaeCKDB0/ECBOVWjTwUvPQ==}
    engines: {node: '>=8'}
    dev: true

  /is-typed-array@1.1.12:
    resolution: {integrity: sha512-Z14TF2JNG8Lss5/HMqt0//T9JeHXttXy5pH/DBU4vi98ozO2btxzq9MwYDZYnKwU8nRsz/+GVFVRDq3DkVuSPg==}
    engines: {node: '>= 0.4'}
    dependencies:
      which-typed-array: 1.1.11
    dev: false

  /is-typedarray@1.0.0:
    resolution: {integrity: sha512-cyA56iCMHAh5CdzjJIa4aohJyeO1YbwLi3Jc35MmRU6poroFjIGZzUzupGiRPOjgHg9TLu43xbpwXk523fMxKA==}
    dev: false

  /isexe@2.0.0:
    resolution: {integrity: sha512-RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw==}
    dev: true

  /isomorphic-ws@4.0.1(ws@7.5.9):
    resolution: {integrity: sha512-BhBvN2MBpWTaSHdWRb/bwdZJ1WaehQ2L1KngkCkfLUGF0mAWAT1sQUQacEmQ0jXkFw/czDXPNQSL5u2/Krsz1w==}
    peerDependencies:
      ws: '*'
    dependencies:
      ws: 7.5.9
    dev: false

  /isomorphic-ws@5.0.0(ws@8.12.0):
    resolution: {integrity: sha512-muId7Zzn9ywDsyXgTIafTry2sV3nySZeUDe6YedVd1Hvuuep5AsIlqK+XefWpYTyJG5e503F2xIuT2lcU6rCSw==}
    peerDependencies:
      ws: '*'
    dependencies:
      ws: 8.12.0
    dev: false

  /jayson@4.1.0:
    resolution: {integrity: sha512-R6JlbyLN53Mjku329XoRT2zJAE6ZgOQ8f91ucYdMCD4nkGCF9kZSrcGXpHIU4jeKj58zUZke2p+cdQchU7Ly7A==}
    engines: {node: '>=8'}
    hasBin: true
    dependencies:
      '@types/connect': 3.4.35
      '@types/node': 12.20.55
      '@types/ws': 7.4.7
      JSONStream: 1.3.5
      commander: 2.20.3
      delay: 5.0.0
      es6-promisify: 5.0.0
      eyes: 0.1.8
      isomorphic-ws: 4.0.1(ws@7.5.9)
      json-stringify-safe: 5.0.1
      uuid: 8.3.2
      ws: 7.5.9
    transitivePeerDependencies:
      - bufferutil
      - utf-8-validate
    dev: false

  /js-sdsl@4.4.1:
    resolution: {integrity: sha512-6Gsx8R0RucyePbWqPssR8DyfuXmLBooYN5cZFZKjHGnQuaf7pEzhtpceagJxVu4LqhYY5EYA7nko3FmeHZ1KbA==}
    dev: true

  /js-tokens@4.0.0:
    resolution: {integrity: sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ==}

  /js-yaml@4.1.0:
    resolution: {integrity: sha512-wpxZs9NoxZaJESJGIZTyDEaYpl0FKSA+FB9aJiyemKhMwkxQg63h4T1KJgUGHpTqPDNRcmmYLugrRjJlBtWvRA==}
    hasBin: true
    dependencies:
      argparse: 2.0.1
    dev: true

  /jsesc@2.5.2:
    resolution: {integrity: sha512-OYu7XEzjkCQ3C5Ps3QIZsQfNpqoJyZZA99wd9aWd05NCtC5pWOkShK2mkL6HXQR6/Cy2lbNdPlZBpuQHXE63gA==}
    engines: {node: '>=4'}
    hasBin: true
    dev: true

  /json-rpc-engine@6.1.0:
    resolution: {integrity: sha512-NEdLrtrq1jUZyfjkr9OCz9EzCNhnRyWtt1PAnvnhwy6e8XETS0Dtc+ZNCO2gvuAoKsIn2+vCSowXTYE4CkgnAQ==}
    engines: {node: '>=10.0.0'}
    dependencies:
      '@metamask/safe-event-emitter': 2.0.0
      eth-rpc-errors: 4.0.2
    dev: false

  /json-rpc-random-id@1.0.1:
    resolution: {integrity: sha512-RJ9YYNCkhVDBuP4zN5BBtYAzEl03yq/jIIsyif0JY9qyJuQQZNeDK7anAPKKlyEtLSj2s8h6hNh2F8zO5q7ScA==}
    dev: false

  /json-schema-traverse@0.4.1:
    resolution: {integrity: sha512-xbbCH5dCYU5T8LcEhhuh7HJ88HXuW3qsI3Y0zOZFKfZEHcpWiHU/Jxzk629Brsab/mMiHQti9wMP+845RPe3Vg==}
    dev: true

  /json-stable-stringify-without-jsonify@1.0.1:
    resolution: {integrity: sha512-Bdboy+l7tA3OGW6FjyFHWkP5LuByj1Tk33Ljyq0axyzdk9//JSi2u3fP1QSmd1KNwq6VOKYGlAu87CisVir6Pw==}
    dev: true

  /json-stringify-safe@5.0.1:
    resolution: {integrity: sha512-ZClg6AaYvamvYEE82d3Iyd3vSSIjQ+odgjaTzRuO3s7toCdFKczob2i0zCh7JE8kWn17yvAWhUVxvqGwUalsRA==}
    dev: false

  /json5@2.2.3:
    resolution: {integrity: sha512-XmOWe7eyHYH14cLdVPoyg+GOH3rYX++KpzrylJwSW98t3Nk+U8XOl8FWKOgwtzdb8lXGf6zYwDUzeHMWfxasyg==}
    engines: {node: '>=6'}
    hasBin: true
    dev: true

  /jsonparse@1.3.1:
    resolution: {integrity: sha512-POQXvpdL69+CluYsillJ7SUhKvytYjW9vG/GKpnf+xP8UWgYEM/RaMzHHofbALDiKbbP1W8UEYmgGl39WkPZsg==}
    engines: {'0': node >= 0.2.0}
    dev: false

  /keccak@3.0.3:
    resolution: {integrity: sha512-JZrLIAJWuZxKbCilMpNz5Vj7Vtb4scDG3dMXLOsbzBmQGyjwE61BbW7bJkfKKCShXiQZt3T6sBgALRtmd+nZaQ==}
    engines: {node: '>=10.0.0'}
    requiresBuild: true
    dependencies:
      node-addon-api: 2.0.2
      node-gyp-build: 4.6.0
      readable-stream: 3.6.2
    dev: false

  /keyvaluestorage-interface@1.0.0:
    resolution: {integrity: sha512-8t6Q3TclQ4uZynJY9IGr2+SsIGwK9JHcO6ootkHCGA0CrQCRy+VkouYNO2xicET6b9al7QKzpebNow+gkpCL8g==}
    dev: false

  /levn@0.4.1:
    resolution: {integrity: sha512-+bT2uH4E5LGE7h/n3evcS/sQlJXCpIp6ym8OWJ5eV6+67Dsql/LaaT7qJBAt2rzfoa/5QBGBhxDix1dMt2kQKQ==}
    engines: {node: '>= 0.8.0'}
    dependencies:
      prelude-ls: 1.2.1
      type-check: 0.4.0
    dev: true

  /lit-element@3.3.2:
    resolution: {integrity: sha512-xXAeVWKGr4/njq0rGC9dethMnYCq5hpKYrgQZYTzawt9YQhMiXfD+T1RgrdY3NamOxwq2aXlb0vOI6e29CKgVQ==}
    dependencies:
      '@lit-labs/ssr-dom-shim': 1.1.1
      '@lit/reactive-element': 1.6.2
      lit-html: 2.7.5
    dev: false

  /lit-html@2.7.5:
    resolution: {integrity: sha512-YqUzpisJodwKIlbMFCtyrp58oLloKGnnPLMJ1t23cbfIJjg/H9pvLWK4XS69YeubK5HUs1UE4ys9w5dP1zg6IA==}
    dependencies:
      '@types/trusted-types': 2.0.3
    dev: false

  /lit@2.7.5:
    resolution: {integrity: sha512-i/cH7Ye6nBDUASMnfwcictBnsTN91+aBjXoTHF2xARghXScKxpD4F4WYI+VLXg9lqbMinDfvoI7VnZXjyHgdfQ==}
    dependencies:
      '@lit/reactive-element': 1.6.2
      lit-element: 3.3.2
      lit-html: 2.7.5
    dev: false

  /locate-path@5.0.0:
    resolution: {integrity: sha512-t7hw9pI+WvuwNJXwk5zVHpyhIqzg2qTlklJOf0mVxGSbe3Fp2VieZcduNYjaLDoy6p9uGpQEGWG87WpMKlNq8g==}
    engines: {node: '>=8'}
    dependencies:
      p-locate: 4.1.0
    dev: false

  /locate-path@6.0.0:
    resolution: {integrity: sha512-iPZK6eYjbxRu3uB4/WZ3EsEIMJFMqAoopl3R+zuq0UjcAm/MO6KCweDgPfP3elTztoKP3KtnVHxTn2NHBSDVUw==}
    engines: {node: '>=10'}
    dependencies:
      p-locate: 5.0.0
    dev: true

  /lodash.isequal@4.5.0:
    resolution: {integrity: sha512-pDo3lu8Jhfjqls6GkMgpahsF9kCyayhgykjyLMNFTKWrpVdAQtYyB4muAMWozBB4ig/dtWAmsMxLEI8wuz+DYQ==}
    dev: false

  /lodash.merge@4.6.2:
    resolution: {integrity: sha512-0KpjqXRVvrYyCsX1swR/XTK0va6VQkQM6MNo7PqW77ByjAhoARA8EfrP1N4+KlKj8YS0ZUCtRT/YUuhyYDujIQ==}
    dev: true

  /loose-envify@1.4.0:
    resolution: {integrity: sha512-lyuxPGr/Wfhrlem2CL/UcnUc1zcqKAImBDzukY7Y5F/yQiNdko6+fRLevlw1HgMySw7f611UIY408EtxRSoK3Q==}
    hasBin: true
    dependencies:
      js-tokens: 4.0.0
    dev: false

  /lottie-react@2.4.0(react-dom@18.2.0)(react@18.2.0):
    resolution: {integrity: sha512-pDJGj+AQlnlyHvOHFK7vLdsDcvbuqvwPZdMlJ360wrzGFurXeKPr8SiRCjLf3LrNYKANQtSsh5dz9UYQHuqx4w==}
    peerDependencies:
      react: ^16.8.0 || ^17.0.0 || ^18.0.0
      react-dom: ^16.8.0 || ^17.0.0 || ^18.0.0
    dependencies:
      lottie-web: 5.12.0
      react: 18.2.0
      react-dom: 18.2.0(react@18.2.0)
    dev: false

  /lottie-web@5.12.0:
    resolution: {integrity: sha512-tt2oiv0EmXC8J/RF877dVCo93vZBBnww+SO6dldREgHD8EsP97jQ42JRryIRfY+6aVESQsHYNEAYgH25cBFy7A==}
    dev: false

  /lru-cache@5.1.1:
    resolution: {integrity: sha512-KpNARQA3Iwv+jTA0utUVVbrh+Jlrr1Fv0e56GGzAFOXN7dk/FviaDW8LHmK52DlcH4WP2n6gI8vN1aesBFgo9w==}
    dependencies:
      yallist: 3.1.1
    dev: true

  /lru-cache@6.0.0:
    resolution: {integrity: sha512-Jo6dJ04CmSjuznwJSS3pUeWmd/H0ffTlkXXgwZi+eq1UCmqQwCh+eLsYOYCwY991i2Fah4h1BEMCx4qThGbsiA==}
    engines: {node: '>=10'}
    dependencies:
      yallist: 4.0.0

  /media-query-parser@2.0.2:
    resolution: {integrity: sha512-1N4qp+jE0pL5Xv4uEcwVUhIkwdUO3S/9gML90nqKA7v7FcOS5vUtatfzok9S9U1EJU8dHWlcv95WLnKmmxZI9w==}
    dependencies:
      '@babel/runtime': 7.22.6
    dev: false

  /merge2@1.4.1:
    resolution: {integrity: sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg==}
    engines: {node: '>= 8'}
    dev: true

  /micromatch@4.0.5:
    resolution: {integrity: sha512-DMy+ERcEW2q8Z2Po+WNXuw3c5YaUSFjAO5GsJqfEl7UjvtIuFKO6ZrKvcItdy98dwFI2N1tg3zNIdKaQT+aNdA==}
    engines: {node: '>=8.6'}
    dependencies:
      braces: 3.0.2
      picomatch: 2.3.1
    dev: true

  /minimalistic-assert@1.0.1:
    resolution: {integrity: sha512-UtJcAD4yEaGtjPezWuO9wC4nwUnVH/8/Im3yEHQP4b67cXlD/Qr9hdITCU1xDbSEXg2XKNaP8jsReV7vQd00/A==}
    dev: false

  /minimatch@3.1.2:
    resolution: {integrity: sha512-J7p63hRiAjw1NDEww1W7i37+ByIrOWO5XQQAzZ3VOcL0PNybwpfmV/N05zFAzwQ9USyEcX6t3UO+K5aqBQOIHw==}
    dependencies:
      brace-expansion: 1.1.11
    dev: true

  /motion@10.16.2:
    resolution: {integrity: sha512-p+PurYqfUdcJZvtnmAqu5fJgV2kR0uLFQuBKtLeFVTrYEVllI99tiOTSefVNYuip9ELTEkepIIDftNdze76NAQ==}
    dependencies:
      '@motionone/animation': 10.15.1
      '@motionone/dom': 10.16.2
      '@motionone/svelte': 10.16.2
      '@motionone/types': 10.15.1
      '@motionone/utils': 10.15.1
      '@motionone/vue': 10.16.2
    dev: false

  /ms@2.1.2:
    resolution: {integrity: sha512-sGkPx+VjMtmA6MX27oA4FBFELFCZZ4S4XqeGOXCv68tT+jb3vk/RyaKWP0PTKyWtmLSM0b+adUTEvbs1PEaH2w==}

  /multiformats@9.9.0:
    resolution: {integrity: sha512-HoMUjhH9T8DDBNT+6xzkrd9ga/XiBI4xLr58LJACwK6G3HTOPeMz4nB4KJs33L2BelrIJa7P0VuNaVF3hMYfjg==}
    dev: false

  /nanoid@3.3.6:
    resolution: {integrity: sha512-BGcqMMJuToF7i1rt+2PWSNVnWIkGCU78jBG3RxO/bZlnZPK2Cmi2QaffxGO/2RvWi9sL+FAiRiXMgsyxQ1DIDA==}
    engines: {node: ^10 || ^12 || ^13.7 || ^14 || >=15.0.1}
    hasBin: true
    dev: true

  /natural-compare-lite@1.4.0:
    resolution: {integrity: sha512-Tj+HTDSJJKaZnfiuw+iaF9skdPpTo2GtEly5JHnWV/hfv2Qj/9RKsGISQtLh2ox3l5EAGw487hnBee0sIJ6v2g==}
    dev: true

  /natural-compare@1.4.0:
    resolution: {integrity: sha512-OWND8ei3VtNC9h7V60qff3SVobHr996CTwgxubgyQYEpg290h9J0buyECNNJexkFm5sOajh5G116RYA1c8ZMSw==}
    dev: true

  /node-addon-api@2.0.2:
    resolution: {integrity: sha512-Ntyt4AIXyaLIuMHF6IOoTakB3K+RWxwtsHNRxllEoA6vPwP9o4866g6YWDLUdnucilZhmkxiHwHr11gAENw+QA==}
    dev: false

  /node-fetch@2.6.12:
    resolution: {integrity: sha512-C/fGU2E8ToujUivIO0H+tpQ6HWo4eEmchoPIoXtxCrVghxdKq+QOHqEZW7tuP3KlV3bC8FRMO5nMCC7Zm1VP6g==}
    engines: {node: 4.x || >=6.0.0}
    peerDependencies:
      encoding: ^0.1.0
    peerDependenciesMeta:
      encoding:
        optional: true
    dependencies:
      whatwg-url: 5.0.0
    dev: false

  /node-gyp-build@4.6.0:
    resolution: {integrity: sha512-NTZVKn9IylLwUzaKjkas1e4u2DLNcV4rdYagA4PWdPwW87Bi7z+BznyKSRwS/761tV/lzCGXplWsiaMjLqP2zQ==}
    hasBin: true
    dev: false

  /node-releases@2.0.12:
    resolution: {integrity: sha512-QzsYKWhXTWx8h1kIvqfnC++o0pEmpRQA/aenALsL2F4pqNVr7YzcdMlDij5WBnwftRbJCNJL/O7zdKaxKPHqgQ==}
    dev: true

  /normalize-path@3.0.0:
    resolution: {integrity: sha512-6eZs5Ls3WtCisHWp9S2GUy8dqkpGi4BVSz3GaqiE6ezub0512ESztXUwUB6C6IKbQkY2Pnb/mD4WYojCRwcwLA==}
    engines: {node: '>=0.10.0'}
    dev: true

  /object-assign@4.1.1:
    resolution: {integrity: sha512-rJgTQnkUnH1sFw8yT6VSU3zD3sWmu6sZhIseY8VX+GRu3P6F7Fu+JNDoXfklElbLJSnc3FUQHVe4cU5hj+BcUg==}
    engines: {node: '>=0.10.0'}
    dev: false

  /object-inspect@1.12.3:
    resolution: {integrity: sha512-geUvdk7c+eizMNUDkRpW1wJwgfOiOeHbxBR/hLXK1aT6zmVSO0jsQcs7fj6MGw89jC/cjGfLcNOrtMYtGqm81g==}
    dev: false

  /on-exit-leak-free@0.2.0:
    resolution: {integrity: sha512-dqaz3u44QbRXQooZLTUKU41ZrzYrcvLISVgbrzbyCMxpmSLJvZ3ZamIJIZ29P6OhZIkNIQKosdeM6t1LYbA9hg==}
    dev: false

  /once@1.4.0:
    resolution: {integrity: sha512-lNaJgI+2Q5URQBkccEKHTQOPaXdUxnZZElQTZY0MFUAuaEqe1E+Nyvgdz/aIyNi6Z9MzO5dv1H8n58/GELp3+w==}
    dependencies:
      wrappy: 1.0.2

  /optionator@0.9.1:
    resolution: {integrity: sha512-74RlY5FCnhq4jRxVUPKDaRwrVNXMqsGsiW6AJw4XK8hmtm10wC0ypZBLw5IIp85NZMr91+qd1RvvENwg7jjRFw==}
    engines: {node: '>= 0.8.0'}
    dependencies:
      deep-is: 0.1.4
      fast-levenshtein: 2.0.6
      levn: 0.4.1
      prelude-ls: 1.2.1
      type-check: 0.4.0
      word-wrap: 1.2.3
    dev: true

  /outdent@0.8.0:
    resolution: {integrity: sha512-KiOAIsdpUTcAXuykya5fnVVT+/5uS0Q1mrkRHcF89tpieSmY33O/tmc54CqwA+bfhbtEfZUNLHaPUiB9X3jt1A==}
    dev: false

  /p-limit@2.3.0:
    resolution: {integrity: sha512-//88mFWSJx8lxCzwdAABTJL2MyWB12+eIY7MDL2SqLmAkeKU9qxRvWuSyTjm3FUmpBEMuFfckAIqEaVGUDxb6w==}
    engines: {node: '>=6'}
    dependencies:
      p-try: 2.2.0
    dev: false

  /p-limit@3.1.0:
    resolution: {integrity: sha512-TYOanM3wGwNGsZN2cVTYPArw454xnXj5qmWF1bEoAc4+cU/ol7GVh7odevjp1FNHduHc3KZMcFduxU5Xc6uJRQ==}
    engines: {node: '>=10'}
    dependencies:
      yocto-queue: 0.1.0
    dev: true

  /p-locate@4.1.0:
    resolution: {integrity: sha512-R79ZZ/0wAxKGu3oYMlz8jy/kbhsNrS7SKZ7PxEHBgJ5+F2mtFW2fK2cOtBh1cHYkQsbzFV7I+EoRKe6Yt0oK7A==}
    engines: {node: '>=8'}
    dependencies:
      p-limit: 2.3.0
    dev: false

  /p-locate@5.0.0:
    resolution: {integrity: sha512-LaNjtRWUBY++zB5nE/NwcaoMylSPk+S+ZHNB1TzdbMJMny6dynpAGt7X/tl/QYq3TIeE6nxHppbo2LGymrG5Pw==}
    engines: {node: '>=10'}
    dependencies:
      p-limit: 3.1.0
    dev: true

  /p-try@2.2.0:
    resolution: {integrity: sha512-R4nPAVTAU0B9D35/Gk3uJf/7XYbQcyohSKdvAxIRSNghFl4e71hVoGnBNQz9cWaXxO2I10KTC+3jMdvvoKw6dQ==}
    engines: {node: '>=6'}
    dev: false

  /p5@1.6.0:
    resolution: {integrity: sha512-RowF+RxfVUhJm/YKXL5TCFzTqnwAIwK6W1VGs9LAqSf3PCmLz9Igbxzlf0Ry5IMV71L42wipCdH/bDiNsqAstA==}
    dev: false

  /parent-module@1.0.1:
    resolution: {integrity: sha512-GQ2EWRpQV8/o+Aw8YqtfZZPfNRWZYkbidE9k5rpl/hC3vtHHBfGm2Ifi6qWV+coDGkrUKZAxE3Lot5kcsRlh+g==}
    engines: {node: '>=6'}
    dependencies:
      callsites: 3.1.0
    dev: true

  /path-exists@4.0.0:
    resolution: {integrity: sha512-ak9Qy5Q7jYb2Wwcey5Fpvg2KoAc/ZIhLSLOSBmRmygPsGwkVVt0fZa0qrtMz+m6tJTAHfZQ8FnmB4MG4LWy7/w==}
    engines: {node: '>=8'}

  /path-is-absolute@1.0.1:
    resolution: {integrity: sha512-AVbw3UJ2e9bq64vSaS9Am0fje1Pa8pbGqTTsmXfaIiMpnr5DlDhfJOuLj9Sf95ZPVDAUerDfEk88MPmPe7UCQg==}
    engines: {node: '>=0.10.0'}
    dev: true

  /path-key@3.1.1:
    resolution: {integrity: sha512-ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==}
    engines: {node: '>=8'}
    dev: true

  /path-type@4.0.0:
    resolution: {integrity: sha512-gDKb8aZMDeD/tZWs9P6+q0J9Mwkdl6xMV8TjnGP3qJVJ06bdMgkbBlLU8IdfOsIsFz2BW1rNVT3XuNEl8zPAvw==}
    engines: {node: '>=8'}
    dev: true

  /picocolors@1.0.0:
    resolution: {integrity: sha512-1fygroTLlHu66zi26VoTDv8yRgm0Fccecssto+MhsZ0D/DGW2sm8E8AjW7NU5VVTRt5GxbeZ5qBuJr+HyLYkjQ==}
    dev: true

  /picomatch@2.3.1:
    resolution: {integrity: sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA==}
    engines: {node: '>=8.6'}
    dev: true

  /pify@3.0.0:
    resolution: {integrity: sha512-C3FsVNH1udSEX48gGX1xfvwTWfsYWj5U+8/uK15BGzIGrKoUpghX8hWZwa/OFnakBiiVNmBvemTJR5mcy7iPcg==}
    engines: {node: '>=4'}
    dev: false

  /pify@5.0.0:
    resolution: {integrity: sha512-eW/gHNMlxdSP6dmG6uJip6FXN0EQBwm2clYYd8Wul42Cwu/DK8HEftzsapcNdYe2MfLiIwZqsDk2RDEsTE79hA==}
    engines: {node: '>=10'}
    dev: false

  /pino-abstract-transport@0.5.0:
    resolution: {integrity: sha512-+KAgmVeqXYbTtU2FScx1XS3kNyfZ5TrXY07V96QnUSFqo2gAqlvmaxH67Lj7SWazqsMabf+58ctdTcBgnOLUOQ==}
    dependencies:
      duplexify: 4.1.2
      split2: 4.2.0
    dev: false

  /pino-std-serializers@4.0.0:
    resolution: {integrity: sha512-cK0pekc1Kjy5w9V2/n+8MkZwusa6EyyxfeQCB799CQRhRt/CqYKiWs5adeu8Shve2ZNffvfC/7J64A2PJo1W/Q==}
    dev: false

  /pino@7.11.0:
    resolution: {integrity: sha512-dMACeu63HtRLmCG8VKdy4cShCPKaYDR4youZqoSWLxl5Gu99HUw8bw75thbPv9Nip+H+QYX8o3ZJbTdVZZ2TVg==}
    hasBin: true
    dependencies:
      atomic-sleep: 1.0.0
      fast-redact: 3.2.0
      on-exit-leak-free: 0.2.0
      pino-abstract-transport: 0.5.0
      pino-std-serializers: 4.0.0
      process-warning: 1.0.0
      quick-format-unescaped: 4.0.4
      real-require: 0.1.0
      safe-stable-stringify: 2.4.3
      sonic-boom: 2.8.0
      thread-stream: 0.15.2
    dev: false

  /pngjs@5.0.0:
    resolution: {integrity: sha512-40QW5YalBNfQo5yRYmiw7Yz6TKKVr3h6970B2YE+3fQpsWcrbj1PzJgxeJ19DRQjhMbKPIuMY8rFaXc8moolVw==}
    engines: {node: '>=10.13.0'}
    dev: false

  /postcss@8.4.24:
    resolution: {integrity: sha512-M0RzbcI0sO/XJNucsGjvWU9ERWxb/ytp1w6dKtxTKgixdtQDq4rmx/g8W1hnaheq9jgwL/oyEdH5Bc4WwJKMqg==}
    engines: {node: ^10 || ^12 || >=14}
    dependencies:
      nanoid: 3.3.6
      picocolors: 1.0.0
      source-map-js: 1.0.2
    dev: true

  /preact@10.16.0:
    resolution: {integrity: sha512-XTSj3dJ4roKIC93pald6rWuB2qQJO9gO2iLLyTe87MrjQN+HklueLsmskbywEWqCHlclgz3/M4YLL2iBr9UmMA==}
    dev: false

  /prelude-ls@1.2.1:
    resolution: {integrity: sha512-vkcDPrRZo1QZLbn5RLGPpg/WmIQ65qoWWhcGKf/b5eplkkarX0m9z8ppCat4mlOqUsWpyNuYgO3VRyrYHSzX5g==}
    engines: {node: '>= 0.8.0'}
    dev: true

  /prettier@2.8.8:
    resolution: {integrity: sha512-tdN8qQGvNjw4CHbY+XXk0JgCXn9QiF21a55rBe5LJAU+kDyC4WQn4+awm2Xfk2lQMk5fKup9XgzTZtGkjBdP9Q==}
    engines: {node: '>=10.13.0'}
    hasBin: true
    dev: true

  /process-warning@1.0.0:
    resolution: {integrity: sha512-du4wfLyj4yCZq1VupnVSZmRsPJsNuxoDQFdCFHLaYiEbFBD7QE0a+I4D7hOxrVnh78QE/YipFAj9lXHiXocV+Q==}
    dev: false

  /prop-types@15.8.1:
    resolution: {integrity: sha512-oj87CgZICdulUohogVAR7AjlC0327U4el4L6eAvOqCeudMDVU0NThNaV+b9Df4dXgSP1gXMTnPdhfe/2qDH5cg==}
    dependencies:
      loose-envify: 1.4.0
      object-assign: 4.1.1
      react-is: 16.13.1
    dev: false

  /proxy-compare@2.5.1:
    resolution: {integrity: sha512-oyfc0Tx87Cpwva5ZXezSp5V9vht1c7dZBhvuV/y3ctkgMVUmiAGDVeeB0dKhGSyT0v1ZTEQYpe/RXlBVBNuCLA==}
    dev: false

  /punycode@2.3.0:
    resolution: {integrity: sha512-rRV+zQD8tVFys26lAGR9WUuS4iUAngJScM+ZRSKtvl5tKeZ2t5bvdNFdNHBW9FWR4guGHlgmsZ1G7BSm2wTbuA==}
    engines: {node: '>=6'}
    dev: true

  /qrcode@1.5.0:
    resolution: {integrity: sha512-9MgRpgVc+/+47dFvQeD6U2s0Z92EsKzcHogtum4QB+UNd025WOJSHvn/hjk9xmzj7Stj95CyUAs31mrjxliEsQ==}
    engines: {node: '>=10.13.0'}
    hasBin: true
    dependencies:
      dijkstrajs: 1.0.3
      encode-utf8: 1.0.3
      pngjs: 5.0.0
      yargs: 15.4.1
    dev: false

  /qrcode@1.5.3:
    resolution: {integrity: sha512-puyri6ApkEHYiVl4CFzo1tDkAZ+ATcnbJrJ6RiBM1Fhctdn/ix9MTE3hRph33omisEbC/2fcfemsseiKgBPKZg==}
    engines: {node: '>=10.13.0'}
    hasBin: true
    dependencies:
      dijkstrajs: 1.0.3
      encode-utf8: 1.0.3
      pngjs: 5.0.0
      yargs: 15.4.1
    dev: false

  /qs@6.11.2:
    resolution: {integrity: sha512-tDNIz22aBzCDxLtVH++VnTfzxlfeK5CbqohpSqpJgj1Wg/cQbStNAz3NuqCs5vV+pjBsK4x4pN9HlVh7rcYRiA==}
    engines: {node: '>=0.6'}
    dependencies:
      side-channel: 1.0.4
    dev: false

  /query-string@6.14.1:
    resolution: {integrity: sha512-XDxAeVmpfu1/6IjyT/gXHOl+S0vQ9owggJ30hhWKdHAsNPOcasn5o9BW0eejZqL2e4vMjhAxoW3jVHcD6mbcYw==}
    engines: {node: '>=6'}
    dependencies:
      decode-uri-component: 0.2.2
      filter-obj: 1.1.0
      split-on-first: 1.1.0
      strict-uri-encode: 2.0.0
    dev: false

  /query-string@7.1.3:
    resolution: {integrity: sha512-hh2WYhq4fi8+b+/2Kg9CEge4fDPvHS534aOOvOZeQ3+Vf2mCFsaFBYj0i+iXcAq6I9Vzp5fjMFBlONvayDC1qg==}
    engines: {node: '>=6'}
    dependencies:
      decode-uri-component: 0.2.2
      filter-obj: 1.1.0
      split-on-first: 1.1.0
      strict-uri-encode: 2.0.0
    dev: false

  /queue-microtask@1.2.3:
    resolution: {integrity: sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A==}
    dev: true

  /quick-format-unescaped@4.0.4:
    resolution: {integrity: sha512-tYC1Q1hgyRuHgloV/YXs2w15unPVh8qfu/qCTfhTYamaw7fyhumKa2yGpdSo87vY32rIclj+4fWYQXUMs9EHvg==}
    dev: false

  /randombytes@2.1.0:
    resolution: {integrity: sha512-vYl3iOX+4CKUWuxGi9Ukhie6fsqXqS9FE2Zaic4tNFD2N2QQaXOMFbuKK4QmDHC0JO6B1Zp41J0LpT0oR68amQ==}
    dependencies:
      safe-buffer: 5.2.1
    dev: false

  /react-dom@18.2.0(react@18.2.0):
    resolution: {integrity: sha512-6IMTriUmvsjHUjNtEDudZfuDQUoWXVxKHhlEGSk81n4YFS+r/Kl99wXiwlVXtPBtJenozv2P+hxDsw9eA7Xo6g==}
    peerDependencies:
      react: ^18.2.0
    dependencies:
      loose-envify: 1.4.0
      react: 18.2.0
      scheduler: 0.23.0
    dev: false

  /react-intersection-observer@9.4.4(react@18.2.0):
    resolution: {integrity: sha512-KQr8ezJscRSQZR0/TjogG4mZttCzdPZj8fhDzAK+xrPYOVvFjabRNy+4EY3UhS3fJaJyIedGjA8y4yKX+nc08w==}
    peerDependencies:
      react: ^15.0.0 || ^16.0.0 || ^17.0.0 || ^18.0.0
    dependencies:
      react: 18.2.0
    dev: false

  /react-is@16.13.1:
    resolution: {integrity: sha512-24e6ynE2H+OKt4kqsOvNd8kBpV65zoxbA4BVsEOB3ARVWQki/DHzaUoC5KuON/BiccDaCCTZBuOcfZs70kR8bQ==}
    dev: false

  /react-refresh@0.14.0:
    resolution: {integrity: sha512-wViHqhAd8OHeLS/IRMJjTSDHF3U9eWi62F/MledQGPdJGDhodXJ9PBLNGr6WWL7qlH12Mt3TyTpbS+hGXMjCzQ==}
    engines: {node: '>=0.10.0'}
    dev: true

  /react-remove-scroll-bar@2.3.4(@types/react@18.0.37)(react@18.2.0):
    resolution: {integrity: sha512-63C4YQBUt0m6ALadE9XV56hV8BgJWDmmTPY758iIJjfQKt2nYwoUrPk0LXRXcB/yIj82T1/Ixfdpdk68LwIB0A==}
    engines: {node: '>=10'}
    peerDependencies:
      '@types/react': ^16.8.0 || ^17.0.0 || ^18.0.0
      react: ^16.8.0 || ^17.0.0 || ^18.0.0
    peerDependenciesMeta:
      '@types/react':
        optional: true
    dependencies:
      '@types/react': 18.0.37
      react: 18.2.0
      react-style-singleton: 2.2.1(@types/react@18.0.37)(react@18.2.0)
      tslib: 2.6.0
    dev: false

  /react-remove-scroll@2.5.4(@types/react@18.0.37)(react@18.2.0):
    resolution: {integrity: sha512-xGVKJJr0SJGQVirVFAUZ2k1QLyO6m+2fy0l8Qawbp5Jgrv3DeLalrfMNBFSlmz5kriGGzsVBtGVnf4pTKIhhWA==}
    engines: {node: '>=10'}
    peerDependencies:
      '@types/react': ^16.8.0 || ^17.0.0 || ^18.0.0
      react: ^16.8.0 || ^17.0.0 || ^18.0.0
    peerDependenciesMeta:
      '@types/react':
        optional: true
    dependencies:
      '@types/react': 18.0.37
      react: 18.2.0
      react-remove-scroll-bar: 2.3.4(@types/react@18.0.37)(react@18.2.0)
      react-style-singleton: 2.2.1(@types/react@18.0.37)(react@18.2.0)
      tslib: 2.6.0
      use-callback-ref: 1.3.0(@types/react@18.0.37)(react@18.2.0)
      use-sidecar: 1.1.2(@types/react@18.0.37)(react@18.2.0)
    dev: false

  /react-style-singleton@2.2.1(@types/react@18.0.37)(react@18.2.0):
    resolution: {integrity: sha512-ZWj0fHEMyWkHzKYUr2Bs/4zU6XLmq9HsgBURm7g5pAVfyn49DgUiNgY2d4lXRlYSiCif9YBGpQleewkcqddc7g==}
    engines: {node: '>=10'}
    peerDependencies:
      '@types/react': ^16.8.0 || ^17.0.0 || ^18.0.0
      react: ^16.8.0 || ^17.0.0 || ^18.0.0
    peerDependenciesMeta:
      '@types/react':
        optional: true
    dependencies:
      '@types/react': 18.0.37
      get-nonce: 1.0.1
      invariant: 2.2.4
      react: 18.2.0
      tslib: 2.6.0
    dev: false

  /react@18.2.0:
    resolution: {integrity: sha512-/3IjMdb2L9QbBdWiW5e3P2/npwMBaU9mHCSCUzNln0ZCYbcfTsGbTJrU/kGemdH2IWmB2ioZ+zkxtmq6g09fGQ==}
    engines: {node: '>=0.10.0'}
    dependencies:
      loose-envify: 1.4.0
    dev: false

  /readable-stream@3.6.2:
    resolution: {integrity: sha512-9u/sniCrY3D5WdsERHzHE4G2YCXqoG5FTHUiCC4SIbr6XcLZBY05ya9EKjYek9O5xOAwjGq+1JdGBAS7Q9ScoA==}
    engines: {node: '>= 6'}
    dependencies:
      inherits: 2.0.4
      string_decoder: 1.3.0
      util-deprecate: 1.0.2
    dev: false

  /readdirp@3.6.0:
    resolution: {integrity: sha512-hOS089on8RduqdbhvQ5Z37A0ESjsqz6qnRcffsMU3495FuTdqSm+7bhJ29JvIOsBDEEnan5DPu9t3To9VRlMzA==}
    engines: {node: '>=8.10.0'}
    dependencies:
      picomatch: 2.3.1
    dev: true

  /real-require@0.1.0:
    resolution: {integrity: sha512-r/H9MzAWtrv8aSVjPCMFpDMl5q66GqtmmRkRjpHTsp4zBAa+snZyiQNlMONiUmEJcsnaw0wCauJ2GWODr/aFkg==}
    engines: {node: '>= 12.13.0'}
    dev: false

  /regenerator-runtime@0.13.11:
    resolution: {integrity: sha512-kY1AZVr2Ra+t+piVaJ4gxaFaReZVH40AKNo7UCX6W+dEwBo/2oZJzqfuN1qLq1oL45o56cPaTXELwrTh8Fpggg==}
    dev: false

  /require-directory@2.1.1:
    resolution: {integrity: sha512-fGxEI7+wsG9xrvdjsrlmL22OMTTiHRwAMroiEeMgq8gzoLC/PQr7RsRDSTLUg/bZAZtF+TVIkHc6/4RIKrui+Q==}
    engines: {node: '>=0.10.0'}
    dev: false

  /require-main-filename@2.0.0:
    resolution: {integrity: sha512-NKN5kMDylKuldxYLSUfrbo5Tuzh4hd+2E8NPPX02mZtn1VuREQToYe/ZdlJy+J3uCpfaiGF05e7B8W0iXbQHmg==}
    dev: false

  /resolve-from@4.0.0:
    resolution: {integrity: sha512-pb/MYmXstAkysRFx8piNI1tGFNQIFA3vkE3Gq4EuA1dF6gHp/+vgZqsCGJapvy8N3Q+4o7FwvquPJcnZ7RYy4g==}
    engines: {node: '>=4'}
    dev: true

  /reusify@1.0.4:
    resolution: {integrity: sha512-U9nH88a3fc/ekCF1l0/UP1IosiuIjyTh7hBvXVMHYgVcfGvt897Xguj2UOLDeI5BG2m7/uwyaLVT6fbtCwTyzw==}
    engines: {iojs: '>=1.0.0', node: '>=0.10.0'}
    dev: true

  /rimraf@3.0.2:
    resolution: {integrity: sha512-JZkJMZkAGFFPP2YqXZXPbMlMBgsxzE8ILs4lMIX/2o0L9UBw9O/Y3o6wFw/i9YLapcUJWwqbi3kdxIPdC62TIA==}
    hasBin: true
    dependencies:
      glob: 7.2.3
    dev: true

  /rollup@3.24.0:
    resolution: {integrity: sha512-OgraHOIg2YpHQTjl0/ymWfFNBEyPucB7lmhXrQUh38qNOegxLapSPFs9sNr0qKR75awW41D93XafoR2QfhBdUQ==}
    engines: {node: '>=14.18.0', npm: '>=8.0.0'}
    hasBin: true
    optionalDependencies:
      fsevents: 2.3.2
    dev: true

  /rpc-websockets@7.5.1:
    resolution: {integrity: sha512-kGFkeTsmd37pHPMaHIgN1LVKXMi0JD782v4Ds9ZKtLlwdTKjn+CxM9A9/gLT2LaOuEcEFGL98h1QWQtlOIdW0w==}
    dependencies:
      '@babel/runtime': 7.22.6
      eventemitter3: 4.0.7
      uuid: 8.3.2
      ws: 8.13.0(bufferutil@4.0.7)(utf-8-validate@5.0.10)
    optionalDependencies:
      bufferutil: 4.0.7
      utf-8-validate: 5.0.10
    dev: false

  /run-parallel@1.2.0:
    resolution: {integrity: sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA==}
    dependencies:
      queue-microtask: 1.2.3
    dev: true

  /rxjs@6.6.7:
    resolution: {integrity: sha512-hTdwr+7yYNIT5n4AMYp85KA6yw2Va0FLa3Rguvbpa4W3I5xynaBZo41cM3XM+4Q6fRMj3sBYIR1VAmZMXYJvRQ==}
    engines: {npm: '>=2.0.0'}
    dependencies:
      tslib: 1.14.1
    dev: false

  /safe-buffer@5.2.1:
    resolution: {integrity: sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ==}
    dev: false

  /safe-json-utils@1.1.1:
    resolution: {integrity: sha512-SAJWGKDs50tAbiDXLf89PDwt9XYkWyANFWVzn4dTXl5QyI8t2o/bW5/OJl3lvc2WVU4MEpTo9Yz5NVFNsp+OJQ==}
    dev: false

  /safe-stable-stringify@2.4.3:
    resolution: {integrity: sha512-e2bDA2WJT0wxseVd4lsDP4+3ONX6HpMXQa1ZhFQ7SU+GjvORCmShbCMltrtIDfkYhVHrOcPtj+KhmDBdPdZD1g==}
    engines: {node: '>=10'}
    dev: false

  /sass@1.63.2:
    resolution: {integrity: sha512-u56TU0AIFqMtauKl/OJ1AeFsXqRHkgO7nCWmHaDwfxDo9GUMSqBA4NEh6GMuh1CYVM7zuROYtZrHzPc2ixK+ww==}
    engines: {node: '>=14.0.0'}
    hasBin: true
    dependencies:
      chokidar: 3.5.3
      immutable: 4.3.0
      source-map-js: 1.0.2
    dev: true

  /scheduler@0.23.0:
    resolution: {integrity: sha512-CtuThmgHNg7zIZWAXi3AsyIzA3n4xx7aNyjwC2VJldO2LMVDhFK+63xGqq6CsJH4rTAt6/M+N4GhZiDYPx9eUw==}
    dependencies:
      loose-envify: 1.4.0
    dev: false

  /semver@6.3.0:
    resolution: {integrity: sha512-b39TBaTSfV6yBrapU89p5fKekE2m/NwnDocOVruQFS1/veMgdzuPcnOM34M6CwxW8jH/lxEa5rBoDeUwu5HHTw==}
    hasBin: true
    dev: true

  /semver@7.5.1:
    resolution: {integrity: sha512-Wvss5ivl8TMRZXXESstBA4uR5iXgEN/VC5/sOcuXdVLzcdkz4HWetIoRfG5gb5X+ij/G9rw9YoGn3QoQ8OCSpw==}
    engines: {node: '>=10'}
    hasBin: true
    dependencies:
      lru-cache: 6.0.0

  /set-blocking@2.0.0:
    resolution: {integrity: sha512-KiKBS8AnWGEyLzofFfmvKwpdPzqiy16LvQfK3yv/fVH7Bj13/wl3JSR1J+rfgRE9q7xUJK4qvgS8raSOeLUehw==}
    dev: false

  /sha.js@2.4.11:
    resolution: {integrity: sha512-QMEp5B7cftE7APOjk5Y6xgrbWu+WkLVQwk8JNjZ8nKRciZaByEW6MubieAiToS7+dwvrjGhH8jRXz3MVd0AYqQ==}
    hasBin: true
    dependencies:
      inherits: 2.0.4
      safe-buffer: 5.2.1
    dev: false

  /shebang-command@2.0.0:
    resolution: {integrity: sha512-kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==}
    engines: {node: '>=8'}
    dependencies:
      shebang-regex: 3.0.0
    dev: true

  /shebang-regex@3.0.0:
    resolution: {integrity: sha512-7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==}
    engines: {node: '>=8'}
    dev: true

  /side-channel@1.0.4:
    resolution: {integrity: sha512-q5XPytqFEIKHkGdiMIrY10mvLRvnQh42/+GoBlFW3b2LXLE2xxJpZFdm94we0BaoV3RwJyGqg5wS7epxTv0Zvw==}
    dependencies:
      call-bind: 1.0.2
      get-intrinsic: 1.2.1
      object-inspect: 1.12.3
    dev: false

  /slash@3.0.0:
    resolution: {integrity: sha512-g9Q1haeby36OSStwb4ntCGGGaKsaVSjQ68fBxoQcutl5fS1vuY18H3wSt3jFyFtrkx+Kz0V1G85A4MyAdDMi2Q==}
    engines: {node: '>=8'}
    dev: true

  /sonic-boom@2.8.0:
    resolution: {integrity: sha512-kuonw1YOYYNOve5iHdSahXPOK49GqwA+LZhI6Wz/l0rP57iKyXXIHaRagOBHAPmGwJC6od2Z9zgvZ5loSgMlVg==}
    dependencies:
      atomic-sleep: 1.0.0
    dev: false

  /source-map-js@1.0.2:
    resolution: {integrity: sha512-R0XvVJ9WusLiqTCEiGCmICCMplcCkIwwR11mOSD9CR5u+IXYdiseeEuXCVAjS54zqwkLcPNnmU4OeJ6tUrWhDw==}
    engines: {node: '>=0.10.0'}
    dev: true

  /split-on-first@1.1.0:
    resolution: {integrity: sha512-43ZssAJaMusuKWL8sKUBQXHWOpq8d6CfN/u1p4gUzfJkM05C8rxTmYrkIPTXapZpORA6LkkzcUulJ8FqA7Uudw==}
    engines: {node: '>=6'}
    dev: false

  /split2@4.2.0:
    resolution: {integrity: sha512-UcjcJOWknrNkF6PLX83qcHM6KHgVKNkV62Y8a5uYDVv9ydGQVwAHMKqHdJje1VTWpljG0WYpCDhrCdAOYH4TWg==}
    engines: {node: '>= 10.x'}
    dev: false

  /stream-browserify@3.0.0:
    resolution: {integrity: sha512-H73RAHsVBapbim0tU2JwwOiXUj+fikfiaoYAKHF3VJfA0pe2BCzkhAHBlLG6REzE+2WNZcxOXjK7lkso+9euLA==}
    dependencies:
      inherits: 2.0.4
      readable-stream: 3.6.2
    dev: false

  /stream-shift@1.0.1:
    resolution: {integrity: sha512-AiisoFqQ0vbGcZgQPY1cdP2I76glaVA/RauYR4G4thNFgkTqr90yXTo4LYX60Jl+sIlPNHHdGSwo01AvbKUSVQ==}
    dev: false

  /strict-uri-encode@2.0.0:
    resolution: {integrity: sha512-QwiXZgpRcKkhTj2Scnn++4PKtWsH0kpzZ62L2R6c/LUVYv7hVnZqcg2+sMuT6R7Jusu1vviK/MFsu6kNJfWlEQ==}
    engines: {node: '>=4'}
    dev: false

  /string-width@4.2.3:
    resolution: {integrity: sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==}
    engines: {node: '>=8'}
    dependencies:
      emoji-regex: 8.0.0
      is-fullwidth-code-point: 3.0.0
      strip-ansi: 6.0.1
    dev: false

  /string_decoder@1.3.0:
    resolution: {integrity: sha512-hkRX8U1WjJFd8LsDJ2yQ/wWWxaopEsABU1XfkM8A+j0+85JAGppt16cr1Whg6KIbb4okU6Mql6BOj+uup/wKeA==}
    dependencies:
      safe-buffer: 5.2.1
    dev: false

  /strip-ansi@6.0.1:
    resolution: {integrity: sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==}
    engines: {node: '>=8'}
    dependencies:
      ansi-regex: 5.0.1

  /strip-json-comments@3.1.1:
    resolution: {integrity: sha512-6fPc+R4ihwqP6N/aIv2f1gMH8lOVtWQHoqC4yK6oSDVVocumAsfCqjkXnqiYMhmMwS/mEHLp7Vehlt3ql6lEig==}
    engines: {node: '>=8'}
    dev: true

  /superstruct@0.14.2:
    resolution: {integrity: sha512-nPewA6m9mR3d6k7WkZ8N8zpTWfenFH3q9pA2PkuiZxINr9DKB2+40wEQf0ixn8VaGuJ78AB6iWOtStI+/4FKZQ==}
    dev: false

  /superstruct@1.0.3:
    resolution: {integrity: sha512-8iTn3oSS8nRGn+C2pgXSKPI3jmpm6FExNazNpjvqS6ZUJQCej3PUXEKM8NjHBOs54ExM+LPW/FBRhymrdcCiSg==}
    engines: {node: '>=14.0.0'}
    dev: false

  /supports-color@5.5.0:
    resolution: {integrity: sha512-QjVjwdXIt408MIiAqCX4oUKsgU2EqAGzs2Ppkm4aQYbjm+ZEWEcW4SfFNTr4uMNZma0ey4f5lgLrkB0aX0QMow==}
    engines: {node: '>=4'}
    dependencies:
      has-flag: 3.0.0
    dev: true

  /supports-color@7.2.0:
    resolution: {integrity: sha512-qpCAvRl9stuOHveKsn7HncJRvv501qIacKzQlO/+Lwxc9+0q2wLyv4Dfvt80/DPn2pqOBsJdDiogXGR9+OvwRw==}
    engines: {node: '>=8'}
    dependencies:
      has-flag: 4.0.0

  /text-encoding-utf-8@1.0.2:
    resolution: {integrity: sha512-8bw4MY9WjdsD2aMtO0OzOCY3pXGYNx2d2FfHRVUKkiCPDWjKuOlhLVASS+pD7VkLTVjW268LYJHwsnPFlBpbAg==}
    dev: false

  /text-table@0.2.0:
    resolution: {integrity: sha512-N+8UisAXDGk8PFXP4HAzVR9nbfmVJ3zYLAWiTIoqC5v5isinhr+r5uaO8+7r3BMfuNIufIsA7RdpVgacC2cSpw==}
    dev: true

  /thread-stream@0.15.2:
    resolution: {integrity: sha512-UkEhKIg2pD+fjkHQKyJO3yoIvAP3N6RlNFt2dUhcS1FGvCD1cQa1M/PGknCLFIyZdtJOWQjejp7bdNqmN7zwdA==}
    dependencies:
      real-require: 0.1.0
    dev: false

  /through@2.3.8:
    resolution: {integrity: sha512-w89qg7PI8wAdvX60bMDP+bFoD5Dvhm9oLheFp5O4a2QF0cSBGsBX4qZmadPMvVqlLJBBci+WqGGOAPvcDeNSVg==}
    dev: false

  /to-fast-properties@2.0.0:
    resolution: {integrity: sha512-/OaKK0xYrs3DmxRYqL/yDc+FxFUVYhDlXMhRmv3z915w2HF1tnN1omB354j8VUGO/hbRzyD6Y3sA7v7GS/ceog==}
    engines: {node: '>=4'}
    dev: true

  /to-regex-range@5.0.1:
    resolution: {integrity: sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==}
    engines: {node: '>=8.0'}
    dependencies:
      is-number: 7.0.0
    dev: true

  /toggle-selection@1.0.6:
    resolution: {integrity: sha512-BiZS+C1OS8g/q2RRbJmy59xpyghNBqrr6k5L/uKBGRsTfxmu3ffiRnd8mlGPUVayg8pvfi5urfnu8TU7DVOkLQ==}
    dev: false

  /tr46@0.0.3:
    resolution: {integrity: sha512-N3WMsuqV66lT30CrXNbEjx4GEwlow3v6rr4mCcv6prnfwhS01rkgyFdjPNBYd9br7LpXV1+Emh01fHnq2Gdgrw==}
    dev: false

  /tslib@1.14.1:
    resolution: {integrity: sha512-Xni35NKzjgMrwevysHTCArtLDpPvye8zV/0E4EyYn43P7/7qvQwPh9BGkHewbMulVntbigmcT7rdX3BNo9wRJg==}

  /tslib@2.6.0:
    resolution: {integrity: sha512-7At1WUettjcSRHXCyYtTselblcHl9PJFFVKiCAy/bY97+BPZXSQ2wbq0P9s8tK2G7dFQfNnlJnPAiArVBVBsfA==}
    dev: false

  /tsutils@3.21.0(typescript@5.0.2):
    resolution: {integrity: sha512-mHKK3iUXL+3UF6xL5k0PEhKRUBKPBCv/+RkEOpjRWxxx27KKRBmmA60A9pgOUvMi8GKhRMPEmjBRPzs2W7O1OA==}
    engines: {node: '>= 6'}
    peerDependencies:
      typescript: '>=2.8.0 || >= 3.2.0-dev || >= 3.3.0-dev || >= 3.4.0-dev || >= 3.5.0-dev || >= 3.6.0-dev || >= 3.6.0-beta || >= 3.7.0-dev || >= 3.7.0-beta'
    dependencies:
      tslib: 1.14.1
      typescript: 5.0.2
    dev: true

  /type-check@0.4.0:
    resolution: {integrity: sha512-XleUoc9uwGXqjWwXaUTZAmzMcFZ5858QA2vvx1Ur5xIcixXIP+8LnFDgRplU30us6teqdlskFfu+ae4K79Ooew==}
    engines: {node: '>= 0.8.0'}
    dependencies:
      prelude-ls: 1.2.1
    dev: true

  /type-fest@0.20.2:
    resolution: {integrity: sha512-Ne+eE4r0/iWnpAxD852z3A+N0Bt5RN//NjJwRd2VFHEmrywxf5vsZlh4R6lixl6B+wz/8d+maTSAkN1FIkI3LQ==}
    engines: {node: '>=10'}
    dev: true

  /typedarray-to-buffer@3.1.5:
    resolution: {integrity: sha512-zdu8XMNEDepKKR+XYOXAVPtWui0ly0NtohUscw+UmaHiAWT8hrV1rr//H6V+0DvJ3OQ19S979M0laLfX8rm82Q==}
    dependencies:
      is-typedarray: 1.0.0
    dev: false

  /typescript@5.0.2:
    resolution: {integrity: sha512-wVORMBGO/FAs/++blGNeAVdbNKtIh1rbBL2EyQ1+J9lClJ93KiiKe8PmFIVdXhHcyv44SL9oglmfeSsndo0jRw==}
    engines: {node: '>=12.20'}
    hasBin: true

  /uint8arrays@3.1.1:
    resolution: {integrity: sha512-+QJa8QRnbdXVpHYjLoTpJIdCTiw9Ir62nocClWuXIq2JIh4Uta0cQsTSpFL678p2CN8B+XSApwcU+pQEqVpKWg==}
    dependencies:
      multiformats: 9.9.0
    dev: false

  /update-browserslist-db@1.0.11(browserslist@4.21.7):
    resolution: {integrity: sha512-dCwEFf0/oT85M1fHBg4F0jtLwJrutGoHSQXCh7u4o2t1drG+c0a9Flnqww6XUKSfQMPpJBRjU8d4RXB09qtvaA==}
    hasBin: true
    peerDependencies:
      browserslist: '>= 4.21.0'
    dependencies:
      browserslist: 4.21.7
      escalade: 3.1.1
      picocolors: 1.0.0
    dev: true

  /uri-js@4.4.1:
    resolution: {integrity: sha512-7rKUyy33Q1yc98pQ1DAmLtwX109F7TIfWlW1Ydo8Wl1ii1SeHieeh0HHfPeL2fMXK6z0s8ecKs9frCuLJvndBg==}
    dependencies:
      punycode: 2.3.0
    dev: true

  /use-callback-ref@1.3.0(@types/react@18.0.37)(react@18.2.0):
    resolution: {integrity: sha512-3FT9PRuRdbB9HfXhEq35u4oZkvpJ5kuYbpqhCfmiZyReuRgpnhDlbr2ZEnnuS0RrJAPn6l23xjFg9kpDM+Ms7w==}
    engines: {node: '>=10'}
    peerDependencies:
      '@types/react': ^16.8.0 || ^17.0.0 || ^18.0.0
      react: ^16.8.0 || ^17.0.0 || ^18.0.0
    peerDependenciesMeta:
      '@types/react':
        optional: true
    dependencies:
      '@types/react': 18.0.37
      react: 18.2.0
      tslib: 2.6.0
    dev: false

  /use-sidecar@1.1.2(@types/react@18.0.37)(react@18.2.0):
    resolution: {integrity: sha512-epTbsLuzZ7lPClpz2TyryBfztm7m+28DlEv2ZCQ3MDr5ssiwyOwGH/e5F9CkfWjJ1t4clvI58yF822/GUkjjhw==}
    engines: {node: '>=10'}
    peerDependencies:
      '@types/react': ^16.9.0 || ^17.0.0 || ^18.0.0
      react: ^16.8.0 || ^17.0.0 || ^18.0.0
    peerDependenciesMeta:
      '@types/react':
        optional: true
    dependencies:
      '@types/react': 18.0.37
      detect-node-es: 1.1.0
      react: 18.2.0
      tslib: 2.6.0
    dev: false

  /use-sync-external-store@1.2.0(react@18.2.0):
    resolution: {integrity: sha512-eEgnFxGQ1Ife9bzYs6VLi8/4X6CObHMw9Qr9tPY43iKwsPw8xE8+EFsf/2cFZ5S3esXgpWgtSCtLNS41F+sKPA==}
    peerDependencies:
      react: ^16.8.0 || ^17.0.0 || ^18.0.0
    dependencies:
      react: 18.2.0
    dev: false

  /utf-8-validate@5.0.10:
    resolution: {integrity: sha512-Z6czzLq4u8fPOyx7TU6X3dvUZVvoJmxSQ+IcrlmagKhilxlhZgxPK6C5Jqbkw1IDUmFTM+cz9QDnnLTwDz/2gQ==}
    engines: {node: '>=6.14.2'}
    requiresBuild: true
    dependencies:
      node-gyp-build: 4.6.0
    dev: false

  /util-deprecate@1.0.2:
    resolution: {integrity: sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw==}
    dev: false

  /util@0.12.5:
    resolution: {integrity: sha512-kZf/K6hEIrWHI6XqOFUiiMa+79wE/D8Q+NCNAWclkyg3b4d2k7s0QGepNjiABc+aR3N1PAyHL7p6UcLY6LmrnA==}
    dependencies:
      inherits: 2.0.4
      is-arguments: 1.1.1
      is-generator-function: 1.0.10
      is-typed-array: 1.1.12
      which-typed-array: 1.1.11
    dev: false

  /uuid@8.3.2:
    resolution: {integrity: sha512-+NYs2QeMWy+GWFOEm9xnn6HCDp0l7QBD7ml8zLUmJ+93Q5NF0NocErnwkTkXVFNiX3/fpC6afS8Dhb/gz7R7eg==}
    hasBin: true
    dev: false

  /valtio@1.10.6(react@18.2.0):
    resolution: {integrity: sha512-SxN1bHUmdhW6V8qsQTpCgJEwp7uHbntuH0S9cdLQtiohuevwBksbpXjwj5uDMA7bLwg1WKyq9sEpZrx3TIMrkA==}
    engines: {node: '>=12.20.0'}
    peerDependencies:
      react: '>=16.8'
    peerDependenciesMeta:
      react:
        optional: true
    dependencies:
      proxy-compare: 2.5.1
      react: 18.2.0
      use-sync-external-store: 1.2.0(react@18.2.0)
    dev: false

  /vanta@0.5.24:
    resolution: {integrity: sha512-fvieEbHy1ZS23zrcX+topzqAgA4Uct1enngOEWLFBgs9TtOf6RDFOYatH7KSVdrABzQDMCQ5myQy+nTSZZwLzg==}
    dev: false

  /viem@1.4.1(typescript@5.0.2):
    resolution: {integrity: sha512-MtaoBHDSJDqa+QyXKG5d+S6EQSebRO0tzw6anSP4zC7AbC614vMeg9Y8LbkmEkWCw8swFYkort+H9l7GkWB0uA==}
    peerDependencies:
      typescript: '>=5.0.4'
    peerDependenciesMeta:
      typescript:
        optional: true
    dependencies:
      '@adraffy/ens-normalize': 1.9.0
      '@noble/curves': 1.0.0
      '@noble/hashes': 1.3.0
      '@scure/bip32': 1.3.0
      '@scure/bip39': 1.2.0
      '@wagmi/chains': 1.6.0(typescript@5.0.2)
      abitype: 0.9.3(typescript@5.0.2)
      isomorphic-ws: 5.0.0(ws@8.12.0)
      typescript: 5.0.2
      ws: 8.12.0
    transitivePeerDependencies:
      - bufferutil
      - utf-8-validate
      - zod
    dev: false

  /vite@4.3.9(sass@1.63.2):
    resolution: {integrity: sha512-qsTNZjO9NoJNW7KnOrgYwczm0WctJ8m/yqYAMAK9Lxt4SoySUfS5S8ia9K7JHpa3KEeMfyF8LoJ3c5NeBJy6pg==}
    engines: {node: ^14.18.0 || >=16.0.0}
    hasBin: true
    peerDependencies:
      '@types/node': '>= 14'
      less: '*'
      sass: '*'
      stylus: '*'
      sugarss: '*'
      terser: ^5.4.0
    peerDependenciesMeta:
      '@types/node':
        optional: true
      less:
        optional: true
      sass:
        optional: true
      stylus:
        optional: true
      sugarss:
        optional: true
      terser:
        optional: true
    dependencies:
      esbuild: 0.17.19
      postcss: 8.4.24
      rollup: 3.24.0
      sass: 1.63.2
    optionalDependencies:
      fsevents: 2.3.2
    dev: true

  /wagmi@1.3.9(react-dom@18.2.0)(react@18.2.0)(typescript@5.0.2)(viem@1.4.1):
    resolution: {integrity: sha512-BQbl+vWLNpLraXd/MWsl1P3I41l7DHrujx6qshIa1HDV7Mdh0GNrDuluRYBtuK2bBx9WM/Fjw45Ef2aKADan9A==}
    peerDependencies:
      react: '>=17.0.0'
      typescript: '>=5.0.4'
      viem: '>=0.3.35'
    peerDependenciesMeta:
      typescript:
        optional: true
    dependencies:
      '@tanstack/query-sync-storage-persister': 4.32.0
      '@tanstack/react-query': 4.32.0(react-dom@18.2.0)(react@18.2.0)
      '@tanstack/react-query-persist-client': 4.32.0(@tanstack/react-query@4.32.0)
      '@wagmi/core': 1.3.8(react@18.2.0)(typescript@5.0.2)(viem@1.4.1)
      abitype: 0.8.7(typescript@5.0.2)
      react: 18.2.0
      typescript: 5.0.2
      use-sync-external-store: 1.2.0(react@18.2.0)
      viem: 1.4.1(typescript@5.0.2)
    transitivePeerDependencies:
      - '@react-native-async-storage/async-storage'
      - bufferutil
      - encoding
      - immer
      - lokijs
      - react-dom
      - react-native
      - supports-color
      - utf-8-validate
      - zod
    dev: false

  /webidl-conversions@3.0.1:
    resolution: {integrity: sha512-2JAn3z8AR6rjK8Sm8orRC0h/bcl/DqL7tRPdGZ4I1CjdF+EaMLmYxBHyXuKL849eucPFhvBoxMsflfOb8kxaeQ==}
    dev: false

  /whatwg-url@5.0.0:
    resolution: {integrity: sha512-saE57nupxk6v3HY35+jzBwYa0rKSy0XR8JSxZPwgLr7ys0IBzhGviA1/TUGJLmSVqs8pb9AnvICXEuOHLprYTw==}
    dependencies:
      tr46: 0.0.3
      webidl-conversions: 3.0.1
    dev: false

  /which-module@2.0.1:
    resolution: {integrity: sha512-iBdZ57RDvnOR9AGBhML2vFZf7h8vmBjhoaZqODJBFWHVtKkDmKuHai3cx5PgVMrX5YDNp27AofYbAwctSS+vhQ==}
    dev: false

  /which-typed-array@1.1.11:
    resolution: {integrity: sha512-qe9UWWpkeG5yzZ0tNYxDmd7vo58HDBc39mZ0xWWpolAGADdFOzkfamWLDxkOWcvHQKVmdTyQdLD4NOfjLWTKew==}
    engines: {node: '>= 0.4'}
    dependencies:
      available-typed-arrays: 1.0.5
      call-bind: 1.0.2
      for-each: 0.3.3
      gopd: 1.0.1
      has-tostringtag: 1.0.0
    dev: false

  /which@2.0.2:
    resolution: {integrity: sha512-BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==}
    engines: {node: '>= 8'}
    hasBin: true
    dependencies:
      isexe: 2.0.0
    dev: true

  /word-wrap@1.2.3:
    resolution: {integrity: sha512-Hz/mrNwitNRh/HUAtM/VT/5VH+ygD6DV7mYKZAtHOrbs8U7lvPS6xf7EJKMF0uW1KJCl0H701g3ZGus+muE5vQ==}
    engines: {node: '>=0.10.0'}
    dev: true

  /wrap-ansi@6.2.0:
    resolution: {integrity: sha512-r6lPcBGxZXlIcymEu7InxDMhdW0KDxpLgoFLcguasxCaJ/SOIZwINatK9KY/tf+ZrlywOKU0UDj3ATXUBfxJXA==}
    engines: {node: '>=8'}
    dependencies:
      ansi-styles: 4.3.0
      string-width: 4.2.3
      strip-ansi: 6.0.1
    dev: false

  /wrappy@1.0.2:
    resolution: {integrity: sha512-l4Sp/DRseor9wL6EvV2+TuQn63dMkPjZ/sp9XkghTEbV9KlPS1xUsZ3u7/IQO4wxtcFB4bgpQPRcR3QCvezPcQ==}

  /ws@7.5.9:
    resolution: {integrity: sha512-F+P9Jil7UiSKSkppIiD94dN07AwvFixvLIj1Og1Rl9GGMuNipJnV9JzjD6XuqmAeiswGvUmNLjr5cFuXwNS77Q==}
    engines: {node: '>=8.3.0'}
    peerDependencies:
      bufferutil: ^4.0.1
      utf-8-validate: ^5.0.2
    peerDependenciesMeta:
      bufferutil:
        optional: true
      utf-8-validate:
        optional: true
    dev: false

  /ws@8.12.0:
    resolution: {integrity: sha512-kU62emKIdKVeEIOIKVegvqpXMSTAMLJozpHZaJNDYqBjzlSYXQGviYwN1osDLJ9av68qHd4a2oSjd7yD4pacig==}
    engines: {node: '>=10.0.0'}
    peerDependencies:
      bufferutil: ^4.0.1
      utf-8-validate: '>=5.0.2'
    peerDependenciesMeta:
      bufferutil:
        optional: true
      utf-8-validate:
        optional: true
    dev: false

  /ws@8.13.0(bufferutil@4.0.7)(utf-8-validate@5.0.10):
    resolution: {integrity: sha512-x9vcZYTrFPC7aSIbj7sRCYo7L/Xb8Iy+pW0ng0wt2vCJv7M9HOMy0UoN3rr+IFC7hb7vXoqS+P9ktyLLLhO+LA==}
    engines: {node: '>=10.0.0'}
    peerDependencies:
      bufferutil: ^4.0.1
      utf-8-validate: '>=5.0.2'
    peerDependenciesMeta:
      bufferutil:
        optional: true
      utf-8-validate:
        optional: true
    dependencies:
      bufferutil: 4.0.7
      utf-8-validate: 5.0.10
    dev: false

  /xtend@4.0.2:
    resolution: {integrity: sha512-LKYU1iAXJXUgAXn9URjiu+MWhyUXHsvfp7mcuYm9dSUKK0/CjtrUwFAxD82/mCWbtLsGjFIad0wIsod4zrTAEQ==}
    engines: {node: '>=0.4'}
    dev: false

  /y18n@4.0.3:
    resolution: {integrity: sha512-JKhqTOwSrqNA1NY5lSztJ1GrBiUodLMmIZuLiDaMRJ+itFd+ABVE8XBjOvIWL+rSqNDC74LCSFmlb/U4UZ4hJQ==}
    dev: false

  /yallist@3.1.1:
    resolution: {integrity: sha512-a4UGQaWPH59mOXUYnAG2ewncQS4i4F43Tv3JoAM+s2VDAmS9NsK8GpDMLrCHPksFT7h3K6TOoUNn2pb7RoXx4g==}
    dev: true

  /yallist@4.0.0:
    resolution: {integrity: sha512-3wdGidZyq5PB084XLES5TpOSRA3wjXAlIWMhum2kRcv/41Sn2emQ0dycQW4uZXLejwKvg6EsvbdlVL+FYEct7A==}

  /yargs-parser@18.1.3:
    resolution: {integrity: sha512-o50j0JeToy/4K6OZcaQmW6lyXXKhq7csREXcDwk2omFPJEwUNOVtJKvmDr9EI1fAJZUyZcRF7kxGBWmRXudrCQ==}
    engines: {node: '>=6'}
    dependencies:
      camelcase: 5.3.1
      decamelize: 1.2.0
    dev: false

  /yargs@15.4.1:
    resolution: {integrity: sha512-aePbxDmcYW++PaqBsJ+HYUFwCdv4LVvdnhBy78E57PIor8/OVvhMrADFFEDh8DHDFRv/O9i3lPhsENjO7QX0+A==}
    engines: {node: '>=8'}
    dependencies:
      cliui: 6.0.0
      decamelize: 1.2.0
      find-up: 4.1.0
      get-caller-file: 2.0.5
      require-directory: 2.1.1
      require-main-filename: 2.0.0
      set-blocking: 2.0.0
      string-width: 4.2.3
      which-module: 2.0.1
      y18n: 4.0.3
      yargs-parser: 18.1.3
    dev: false

  /yocto-queue@0.1.0:
    resolution: {integrity: sha512-rVksvsnNCdJ/ohGc6xgPwyN8eheCxsiLM8mxuE/t/mOVqJewPuO1miLpTHQiRgTKCLexL4MeAFVagts7HmNZ2Q==}
    engines: {node: '>=10'}
    dev: true

  /zustand@4.3.9(react@18.2.0):
    resolution: {integrity: sha512-Tat5r8jOMG1Vcsj8uldMyqYKC5IZvQif8zetmLHs9WoZlntTHmIoNM8TpLRY31ExncuUvUOXehd0kvahkuHjDw==}
    engines: {node: '>=12.7.0'}
    peerDependencies:
      immer: '>=9.0'
      react: '>=16.8'
    peerDependenciesMeta:
      immer:
        optional: true
      react:
        optional: true
    dependencies:
      react: 18.2.0
      use-sync-external-store: 1.2.0(react@18.2.0)
    dev: false
