<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
        <head>
            <title>Listado de Coches</title>
        </head>
        <body>
            <h1>Lista de Coches</h1>
            <ul>
                <xsl:for-each select="coches/coche">
                    <li>
                        <b><xsl:value-of select="marca"/></b> -
                        <xsl:value-of select="modelo"/> -
                        <xsl:value-of select="año"/> -
                        <xsl:value-of select="motor"/>
                    </li>
                </xsl:for-each>
            </ul>
        </body>
        </html>
    </xsl:template>

</xsl:stylesheet>