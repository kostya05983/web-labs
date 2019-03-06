package itzoo.controller

import org.springframework.web.bind.annotation.CrossOrigin
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController

@RestController
class ModelController {

    companion object {
        val producers = mapOf(
            Pair(
                "Samsung", arrayOf(
                    "Твердотельный накопитель samsung 850",
                    "Твердотельный накопитель Samsung MZ-76E250BW",
                    "Твердотельный накопитель Samsung MZ-V7E250BW",
                    "Твердотельный накопитель Samsung MZ-V7E500BW"
                )
            ),
            Pair(
                "WesternDigital", arrayOf(
                    "Твердотельный накопитель Western Digital WD GREEN PC SSD 240 GB (WDS240G2G0A)",
                    "Твердотельный накопитель Western Digital WD GREEN PC SSD 480 GB (WDS480G2G0A)",
                    "Твердотельный накопитель Western Digital WD BLUE 3D NAND SATA SSD 500 GB (WDS500G2B0A)",
                    "Твердотельный накопитель Western Digital WD GREEN PC SSD 120 GB (WDS120G2G0B)"
                )
            ),
            Pair(
                "Kingston", arrayOf(
                    "Твердотельный накопитель Kingston SA400S37/120G",
                    "Твердотельный накопитель Kingston SA1000M8/240G",
                    "Твердотельный накопитель Kingston SUV500/120G",
                    "Твердотельный накопитель Kingston SA1000M8/480G"
                )
            ),
            Pair(
                "Intel", arrayOf(
                    "Твердотельный накопитель Intel SSDSC2KW256G8X1",
                    "Твердотельный накопитель Intel SSDSC2KW256G8",
                    "Твердотельный накопитель Intel SSDSC2KW512G8",
                    "Твердотельный накопитель Intel SSDSC2KB240G801"
                )
            )
        )
    }

    @CrossOrigin
    @RequestMapping("/models")
    fun producers(@RequestParam("producer") producer: String): Array<String>? {
        return producers[producer]
    }

    @CrossOrigin
    @RequestMapping("/producer")
    fun selectMessage(@RequestParam("producer") producer: String, @RequestParam("model") model: String): String {
        return "Вы выбрали следующий ssd: модель $model, производителя $producer"
    }
}